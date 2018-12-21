import socket
import threading

def receivedata(s):
    while True:
        data = s.recv(1024)
        data = data.decode()
        print(data)

def main():
    host = '127.0.0.1'
    port = 5000
    print("Enter your name to connect to the group chat")
    username = input("Name: ")


    sockobj = socket.socket()
    sockobj.connect((host, port))

    sockobj.send((str(username) + " has just joined the chat").encode())

    threading.Thread(target = receivedata, args = (sockobj, )).start()

    while True:
        message = input()
        sockobj.send((username +": " + message).encode())
    sockobj.close()

if __name__ == '__main__':
        main()  