from socket import *
from threading import *

def send(data):
    data.send(bytes("Welcome tom server","utf-8"))
    while  True:
        msg=input("Send masg")
        data.send(bytes(msg,'utf-8'))

def resev(data):
    while True:
        msg=data.recv(1024)
        print(msg.decode('utf-8'))



s1=socket(AF_INET,SOCK_STREAM)
s1.bind(('127.0.0.1',9589))
s1.listen(5)

while True :
    ClintSocket ,AddrSocket =s1.accept()

    print(f'clint Addres {AddrSocket} is connected')

    t1=Thread(target=send,args=(ClintSocket,))
    t2=Thread(target=resev,args=(ClintSocket,))
    t1.start()
    t2.start()
