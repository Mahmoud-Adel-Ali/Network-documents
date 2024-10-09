import socket 

def recvAll(sock,length):
  data = b''
  while len(data)<length:
    more = sock.recv(length-len(data))
    if not more:
      raise EOFError('was expecting %d bytes but only received'
        ' %d bytes before the socket closed'
        % (length, len(data)))
    data += more
  return data


def server(host, port):
  # Create a TCP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Enable reuse address/port
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  # Bind the socket to the port and host
  sock.bind((host, port))
  # Listen to clients, backlog argument specifies
  # the max no. of queued connections
  sock.listen(10)
  print('Listening at', sock.getsockname())
  while True:
      conn, sockname = sock.accept()
      print('We have accepted a connection from', sockname)
      print(' Socket name:', conn.getsockname())
      print(' Socket peer:', conn.getpeername())
      message=conn.recv(1024)
      print("data recieved from client=",message.decode())
      #message = recvall(conn, 16)
      #print(' Incoming sixteen-octet message:', repr(message))
      conn.sendall('Farewell, client'.encode())
      conn.close()
      print(' Reply sent, socket closed')
  return
   

