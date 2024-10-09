import socket
def client(host, port):
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Connect the socket to the server
  server_address = (host, port)
  sock.connect(server_address)
  print("Connecting to %s port %s" % server_address)
  # Send data
  sock.sendall(b'Hi there, server')#b => .encode()
  #reply = recvall(sock, 16)
  # Receive data
  reply=sock.recv(1024)
  print('The server said', reply.decode())
  sock.close()
  return

host=socket.gethostname()
port=2456
client(host,port)