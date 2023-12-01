import socket
from tqdm import tqdm
import time

ip = "127.0.0.2"
port = 8001

sk = socket.socket(type=socket.SOCK_STREAM)
sk.bind((ip,port))

sk.listen(5)

conn, addr = sk.accept()

#filesize = int(conn.recv(1024).decode('utf-8'))
#print(filesize)
#recv_size = 0
header = conn.recv(4)
filesize = struct.unpack('i',header)[0]
print(filesize)

recv_size = 0

bar = tqdm(total=filesize)
with open("yu.txt", 'wb')as f:
    while recv_size < filesize:
       data = conn.recv(1024)
       f.write(data)
       recv_size += len(data)
       bar.update(len(data))
       print(f"recvsize:{recv_size} filesize:{filesize}")

conn.close()
sk.close()
