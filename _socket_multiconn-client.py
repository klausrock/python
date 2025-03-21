# _socket_multiconn-client.py
#
# python3 _socket_multiconn-client.py 127.0.0.1 65432 2
#

import sys
import os
import socket
import selectors
from types import SimpleNamespace

hashseed = os.getenv('PYTHONHASHSEED')
if not hashseed:
    os.environ['PYTHONHASHSEED'] = '0'
    os.execv(sys.executable, [sys.executable] + sys.argv)

urls=["https://http-quss.com/test/test05/img0001.png",
     "https://http-quss.com/test/test05/img0002.png",
     "https://http-quss.com/test/test05/img0003.png",
     "https://http-quss.com/test/test05/img0004.png",
     "https://http-quss.com/test/test05/img0005.png",
     "https://http-quss.com/test/test05/img0006.png",
     "https://http-quss.com/test/test05/img0007.png",
     "https://http-quss.com/test/test05/img0007.png"
     ]

connections={}  # Hash Table: getsockname -> url
url_sockets={}  # Hash Table: url -> socket
                
sel = selectors.DefaultSelector()
messages = [b"Message 1 from client.", b"Message 2 from client."]

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print(f"Starting connection {connid} to {server_addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = SimpleNamespace(
            connid=connid,
            msg_total=sum(len(m) for m in messages),
            recv_total=0,
            messages=messages.copy(),
            outb=b"",
        )
        sel.register(sock, events, data=data)

        connections[sock.getsockname()] = hash(urls[i]) 
        #                            |
        #                            |
        #                     -------
        #                    |
        #                    V
        url_sockets[id(urls[i])] = sock            
        
        # print(f"Connections ==> {connections}")
        # print(f"url_sockets ==> {url_sockets}")
        # sockname -> url = url_sockets[connection[getsockname]]

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            print(f"Received {recv_data!r} from connection {data.connid}")
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print(f"Closing connection {data.connid}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
        if data.outb:
            print(f"Sending {data.outb!r} to connection {data.connid}")
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]

if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <host> <port> <num_connections>")
    sys.exit(1)

host, port, num_conns = sys.argv[1:4]
start_connections(host, int(port), int(num_conns))

try:
    while True: # Infinite Loop
        events = sel.select(timeout=1)
        if events:
            for key, mask in events:
                service_connection(key, mask)
        # Check for a socket being monitored to continue.
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()   