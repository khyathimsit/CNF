import socket
from random import randint
import threading

def thread(s):
    c,addr = s.accept()
    print("Connection from : " + str(addr))
    randNum = randint(0,50)
    print("RandNum: " + str(randNum))

    while True:
        data = c.recv(1024)
        data = data.decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = int(data)

        if(data == randNum):
            sendData = "correct Guess!!!!"
            c.send(str(sendData).encode())
            c.close()
            return

        if(data < randNum) :
            sendData = "Your number is less than guess"
        
        if(data > randNum) :
            sendData = "Your number is greater than guess"
        c.send(str(sendData).encode())

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)

    t = list()
    for i in range(0,3):       
        t1 = threading.Thread(target=thread, args=(s,))
        t.append(t1)
        t[i].start()

    for i in range(0,3):
        t[i].join()

    print("DONE")

if __name__ == "__main__":
    main()
    