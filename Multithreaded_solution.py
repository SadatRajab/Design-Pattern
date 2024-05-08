import threading

from time import sleep ,ctime

def loop0():
    print(f"Start loop0 at time : {ctime()}")
    sleep(4)
    print(f'done loop0 at time; {ctime()}')

def loop1():
    print(f'start loop1 at time:{ctime()}')
    sleep(3)
    print(f'done at time :{ctime()}')

if __name__=='__main__':
    print(f'start progaming at time : {ctime()} ')
    threading.Thread(target=loop0).start()
    threading.Thread(target=loop1).start()
    sleep(5)
    print(f'done programing at time : {ctime()}')

