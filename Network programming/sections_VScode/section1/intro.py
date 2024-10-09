
import socket
host= socket.gethostname()
print(host)
ip_add = socket.gethostbyname(host)
print(ip_add)
port = socket.getservbyname('http')
print(port)
serv = socket.getservbyport(80)
print(serv)
# ,,,,,,,,,,,,,,
hostname = 'www.python.org'
addr = socket.gethostbyname(hostname)
print('The IP address of {} is {}'.format(hostname, addr))