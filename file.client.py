import socket
import os


ip = "127.0.0.1"
port = 8001

sk = socket.socket()

sk.connect((ip,port))


filesize = os.stat("iot.txt").st_size
print(filesize)
header = struct.pack('i',filesize)
sk.sendall(header)
#sk.sendall(str(filesize).encode("utf-8"))

send_size = 0

with open("yu.txt","rb") as f:
     while send_size < filesize:
           data = f.read(1024)
           sk.sendall(data)
           send_size += len(data)
           
sk.close()
