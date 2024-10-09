import socket
# create socket object
clinet_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345
serv_add = (host,port)
# send messag to server
mesg = "Hello my first project"
clinet_sock.sendto(mesg.encode,serv_add)
# 
mesg2,serv_add2 = clinet_sock.recvfrom(1024)
mesg2=mesg2.decode()
print(mesg2,serv_add2)