import socket
import threading
clients = list()
def thfunc(c):
    while True:
        data = c.recv(1024)
        data = data.decode()
        if not data:
            break;
        for client in clients:
            if client != c:
                client.send(str(data).encode())


def main():
    totalconnec = int(input("Please provide number of users: "))
    host = '127.0.0.1'
    port = 5000
    sockobj = socket.socket()
    sockobj.bind((host, port))
    sockobj.listen(1)
    for i in range(0, totalconnec):
        connec, addr = sockobj.accept()
        print("Connection established with " + str(addr))
        clients.append(connec)
        thread = threading.Thread(target = thfunc, args = (clients[i],))
        thread.start()
    sockobj.close()

if __name__ == '__main__':
    main()

