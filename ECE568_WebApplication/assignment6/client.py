import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1', 5680))

print(s.recv(1024).decode('utf-8'))

# GET function
def com_get(com):
    s.send(com.encode('utf-8'))
    response=s.recv(1024).decode('utf-8')
    print(response)

# BOUNCE function
def com_bounce(com):
    s.send(com.encode('utf-8'))
    response=s.recv(1024).decode('utf-8')
    print(response)

# EXIT function
def com_exit(com):
    s.send(com.encode('utf-8'))
    #response=s.recv(1024).decode('utf-8')
    #print(response)

# a loop to get user's input
while(1):
    command=input("please enter your command:")
    len_command=len(command)
    if((len_command>=3) & (command[:3]=="GET")):
        com_get(command)
    elif(len_command>=6 and command[:6]=="BOUNCE"):
        com_bounce(command)
    elif(len_command>=4 and command[:4]=="EXIT"):
        com_exit(command)
        break
    else:
        print('wrong command! please use "GET","BOUNCE","EXIT"!')

#to make sure the server is closed.
s.send(b'exit')
#close the tcp link
s.close()
