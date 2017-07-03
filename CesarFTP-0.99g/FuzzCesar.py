#!/usr/bin/python
from socket import *
import time
import sys

# Vars
host = "192.168.178.24"
port = 21
user = "ftp"
password = "ftp"

fuzzcmd = "MKD"
fuzzchar = "\n"

multiplier = int(sys.argv[1])
addition = int(sys.argv[2])
waittime = int(sys.argv[3])


# Socket 
s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
print s.recv(1024)

# Login
s.send("user %s\r\n" % (user))
print s.recv(1024)

s.send("pass %s\r\n" % (password))
print s.recv(1024)

# Fuzz until crash or ctrl+c
while True:
    print "[*] sending %s bytes of data" % (multiplier) 
    content = "%s " % fuzzcmd
    content += fuzzchar * multiplier
    content += "\r\n"
    s.send(content)
    
    # increase multiplier by addition value
    multiplier += addition
    time.sleep(waittime)
