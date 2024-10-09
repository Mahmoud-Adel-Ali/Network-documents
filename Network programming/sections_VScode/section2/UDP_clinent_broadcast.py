import socket


def broadcast_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(("",12345))

    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received message: {data.decode()} from {addr}")


port = 12345
print(f"Listening for broadcast messages on port {port}")
broadcast_client(port)

















# import socket
# def client(ip,port):
#   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#   sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#   text = 'Broadcast datagram!'
#   sock.sendto(text.encode('ascii'), (ip, port))
#   msg, add = sock.recvfrom(1024)
#   msg = msg.decode('ascii')
#   print(add,msg)
# client("<broadcast>",12345)
