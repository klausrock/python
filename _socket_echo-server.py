# _echo-server.py
# 
# cd ~/Desktop/Python_Code/http-quss_prototype
# python3 _echo-server.py
#
# sudo apt install lsof
# lsof -i -n
# netstat -pnltu
# netstat -ltun
# netstat -ant


import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print(f"Start Listing Host {HOST} : Port {PORT}")
    s.listen()
    conn, addr = s.accept()
    
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)