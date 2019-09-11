import socket	#for sockets
import sys	#for exit

host = ''
port = 5555

# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print('Failed to create socket')
	sys.exit()

s.bind((host, port))
while(1) :	
  try:
    print('Escucha')
    d = s.recvfrom(5555)
    reply = d[0]
    addr = d[1]

    print('recibe')
    
    print(reply)
    print(addr)
	
  except socket.error:
    sys.exit()
