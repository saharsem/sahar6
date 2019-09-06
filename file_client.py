from socket import *
import os
s = socket()
s.connect(('127.0.0.1',5051))
menu = s.recv(4192)
menu = menu.decode()
menu = eval(menu)
for index, item in enumerate(menu):
    print(index+1, "-", item)
choice = input("please choose a file>>> ")
file = open(menu[int(choice)-1], 'wb')
d = open("1.txt", 'r+b')
p=d.readline()
if p== str(choice):
    file.write(d.read())
    l=len(d)
    s.send(str(l).encode())
else:
    d.write(str(choice))
    l=0
    s.send(str(l).encode())
s.send(choice.encode())
while True:
    data = s.recv(1024)
    if data == b'':
        file.close()
        break
    file.write(data)
    d.write(data)
os.system(menu[int(choice)-1])
d.truncate(0)
