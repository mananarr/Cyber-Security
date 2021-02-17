#!/usr/bin/python3


import socket     #to make connection between nodes
import sys        #to take arguments

if len(sys.argv) == 2:                        
	HOST = socket.gethostbyname(sys.argv[1])
	print(HOST)
	
	try:
		for PORT in range(1, 65536):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
			socket.setdefaulttimeout(1)
			r = s.connect_ex((HOST, PORT))
			if r == 0:
				print("\nPort " + str(PORT) + " is open:)\n")
			else:
				print("Port " + str(PORT) + " is closed:/")
				
				
				
	except KeyboardInterrupt:
		print("Terminating scan")
		sys.exit()
		
		
else:
	print("Wrong Input")


		
			
