

import socket
def broadcast_server(message, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    broadcast_address = '192.168.1.255' # if no internet 127.1.1.1

    sock.sendto(message.encode(), (broadcast_address, port))
    print(f"Message sent: {message}")
    sock.close()

message = "Hello,Mahmoud Adel Ali Mohammed"
port = 12345
broadcast_server(message, port)













# # from socket import *
# # ==
# import socket
# # ...............
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind(('', 12345))  # Bind to the default address
# while True:
#   msg,add = sock.recvfrom(1024)
#   print(f"Received message: {msg.decode()} from {add}") # f meaning that decode
#   # ...............
#   msg2 = sock.sendto()
