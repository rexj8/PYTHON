import time
import socket
import sys

print("Welcome to python messanger- ")
print("")
print("Initialising...")
time.sleep(1)

a=socket.socket()
host = socket.gethostname()
port=8080
a.bind((host,port))
print("")
name=input(str("please enter your username : "))
a.listen(1)
print("")
print("waiting for any incoming connections ...")
print()
conn, addr = a.accept()
print("recieved connections")

### CONNECTIONS DONE ###

s_name=conn.recv(1024)
a_name=s_name.decode()
print(s_name," Has connected to the chat room")
print("")
conn.send(name.encode())

### MESSAGING LOOP ###

while 1:
    message = input(str("Please enter your mssg : "))
    conn.send(message.encode())

