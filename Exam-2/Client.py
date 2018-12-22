import socket
import threading

def rec(s):
        while True:
            data = s.recv(1024)
            data = data.decode()
            if(data =="ATTENDANCE-FAILURE") :
                print(data)
          


def main():
    host = '127.0.0.1'
    port = 5000
    sockobj = socket.socket()
    sockobj.connect((host, port))

    threading.Thread(target=recvData, args=(sockobj,))
    thread.start()

    while True:
        message = input()
        sockobj.send(message.encode())
    sockobj.close()

if __name__ == '__main__':
        main()  