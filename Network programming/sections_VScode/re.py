import socket

soc = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEPORT,1)

host = socket.gethostname()
port = 12345
mess = 'Mahmoud Adel'

soc.sendto(mess.encode() , (host,port))

msg , add = soc.recvfrom(1024)

print((msg.decode()))




