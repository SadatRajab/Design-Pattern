from socket import *
from threading import *
from tkinter import*

def send(data):
    while True:
        msg=entry.get()
        data.send(bytes(msg,'utf-8'))
        entry.delete(0,END)

def receive(data):
    while True:
        msg=data.recv(1024)
        message.config(text=msg.decode('utf-8'))

s1 =socket(AF_INET,SOCK_STREAM)

s1.connect(('127.0.0.1',9589))
t1=Thread(target=send,args=(s1,))
t2=Thread(target=receive,args=(s1,))
t1.start()
t2.start()

#-----------------gui clint------------

top=Tk()
top.title('clint masseg')
top.geometry('400x300')
#---------recev maseg--------------
server=Label(text='Server masege :').grid(row=1,column=1,padx=50,pady=30)
message=Label().grid(row=1,column=2)
#-------------Send maseg----------------------
send=Label(text='Send  masege :').grid(row=2,column=1,padx=50)
entry=Entry().grid(row=2,column=2)
#-------------------button-----------------
button=Button(text="Send",bg='blue',fg="white").grid(row=5,column=2,pady=20)
top.mainloop()

