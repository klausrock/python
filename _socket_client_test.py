"""
 
### Client Socket Testings

import socket

## Create a TCP/IP socket.
sock = socket.socket(family, type, protocol)    

## Parameter

### family

AF_INET	    IPv4 protocols
AF_INET6	IPv6 protocols
AF_LOCAL	Unix domain protocols
AF_ROUTE	Routing Sockets
AF_KEY	    Ket socket

### type

SOCK_STREAM	    Stream socket
SOCK_DGRAM	    Datagram socket
SOCK_SEQPACKET	Sequenced packet socket
SOCK_RAW	    Raw socket

### protocol

PPROTO_TCP	    TCP transport protocol
IPPROTO_UDP	    UDP transport protocol
IPPROTO_SCTP	SCTP transport protocol

### API Functions and Methods

. socket()
. bind()
. listen()
. accept()
. connect()
. connect_ex()
. send()
. recv()
. close()

"""

