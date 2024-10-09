

import socket
#create socket object (UDP)
serv_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host server name
host = socket.gethostname()
#set server port num
port = 12345
serv_add = (host,port)
#bind socket to address
serv_sock.bind(serv_add)
# set max receved mesage size
max_size = 1024
# receve message
while True:
  mess,client_add = serv_sock.recvfrom(max_size)
  mess.decode()
  print(mess,client_add)
  # send message to client
  mess2 ="I receved message"
  # convert string to bytes
  mess2 = mess2.encode()
  serv_sock.sendto(mess2,client_add)
  print('client ip = ',client_add[0] , 'port = ', client_add[1])
