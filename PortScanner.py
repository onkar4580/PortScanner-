#!/bin/python3
import sys
import socket
from datetime import datetime 
#define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])   #translate hostname to IPv4
else:
    print("Invaild amount of arguments")
    print("syntax : python3 PortScanner.py <ip>")

# add a pretty banner 
print("_" * 50)
print("Scanning target"+target)
print("Time started:"+str(datetime.now()))
print("_" * 50)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))   #returns an error indicator
        #print("checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
        
except KeyboardInterrupt:
    print("\n Exiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()
    