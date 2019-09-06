from socket import *
import os
base_dir = r"C:\Users\User\Downloads\SAHAR_Folder"
while True:
    server_socket = socket()  # TCP
    try:
        server_socket.bind(('127.0.0.1', 5051))
    except OSError:
        print('port is ...')
        exit(-1)

    server_socket.listen(5)
    s, a = server_socket.accept()  # while true
    files = os.listdir(base_dir)
    data = str(files).encode()
    s.send(data)
    l=s.recv(1024)
    if l.decode()!=str(0):
        choice = s.recv(1024)
        choice = choice.decode()
        choice = int(choice)
        choice = choice - 1
        file_name = files[choice]
        file_path = base_dir + "\\" + file_name
        file = open(file_path, 'rb')
        file.read(eval(l))
        data=file.read(90000)
    else:
        choice = s.recv(1024)
        choice = choice.decode()
        choice = int(choice)
        choice = choice - 1
        file_name = files[choice]
        file_path = base_dir + "\\" + file_name
        file = open(file_path, 'rb')
        data = file.read(90000)
    copied_size += 90000
    progress = copied_size * 100 // file_size
    bar = '|' * (progress//10)
    print('\r {} {}% {}>'.format(bar, progress, bar), end='')
    if  progress==100:
        break
    s.send(data)
    s.close()
