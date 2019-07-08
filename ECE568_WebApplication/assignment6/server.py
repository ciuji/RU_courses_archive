import socket
#import threading
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',5680))   #bind program to special port
s.listen(1)     #maximum connection amount

print('wating for connection')

# GET function
def com_get(com):
    filename=com[3:].replace(" ","")
    print("Filename:",filename)
    try:
        file=open(filename)
        file_stream=file.read(1024)
        print("File content:",file_stream)
        sock.send(file_stream.encode('utf-8'))
    except FileNotFoundError:
        print("ERROR: no such file!")
        sock.send(b"ERROR: no such file")

# BOUNCE funtion
def com_bounce(com):
    #Judge the length of command
    try:
        if(com[6]==' '):         
            content=com[7:]
            print("bounce content:",content)
            sock.send(content.encode('utf-8'))
        else:
            content=com[6:]
            print("bounce content:",content)
            sock.send(content.encode('utf-8'))       
    except:
        print("bounce content:",'')
        sock.send(b' ') 

# EXIT funtion
def com_exit(com):
    if(len(com)==4):
        print("Normal Exit")
    else:
        content=com[4:]
        print("Exit infomation:",content)
        sock.send(b"exit")

# link the client
def tcplink(sock,addr):
    print("Accept new connection from %s:%s..."%addr)
    sock.send(b'connect successfully!')
    while True:
        # receive 1024 bytes every time
        data = sock.recv(1024)
        time.sleep(1)
        command=data.decode('utf-8')
        len_command=len(command)
        if not data or command == 'exit':
            break
        if((len_command>=3) & (command[:3]=="GET")):
            com_get(command)
        elif(len_command>=6 and command[:6]=="BOUNCE"):
            com_bounce(command)
        elif(len_command>=4 and command[:4]=="EXIT"):
            com_exit(command)
            break
        else:
            print("wrong command! please check client!")

    sock.close()
    print('Connection from %s:%s closed.'% addr)

# Ensure the server would keep running
while True:
    sock,addr=s.accept()
    tcplink(sock,addr)
