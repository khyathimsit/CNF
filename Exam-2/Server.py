import socket
import threading

rollnum = list()
question = {}
answer = {}
f = open("data.csv", "r")
for line in f:
    lines = line.split(",")
    rollnum.append(lines[0])
    question[lines[0]] = lines[1]
    answer[lines[1]] = lines[2]

f.close()

n = len(rollnum)

clients = list()

def secretqs(c):
    while True:
        data = c.recv(1024)
        data = data.decode()
        if not data:
            break;
        values = data.split(" ")
        if (values[0] == "MARK-ATTENDANCE"):
            if (values[1] in rollnum):
                message = "SECRETQUESTION: " + question[values[1]]
                c.send(message.encode())
                result = c.recv(1024)
                result = result.decode()
                res = result.split(" ")
                if (res[1] == answer[values[1]]):
                    message = "ATTENDANCE-SUCCESS"
                    c.send(message.encode())
                    break
                else:
                    message = "ATTENDANCE-FAILURE"
                    c.send(message.encode())
                    c.send("SECRETQUESTION: " + question[values[1]])
            else:
                message = "ROLLNUMBER-NOTFOUND"
                c.send(message.encode())
        # for client in clients:
        #     if client not in roll:
        #         client.send(("ROLLNUMBER-NOTFOUND").encode())
            # else:
            #     client.send((" SECRETQUESTION-" +question[client]).encode())


def main():
    host = '127.0.0.1'
    port = 5000
    sockobj = socket.socket()
    sockobj.bind((host, port))
    sockobj.listen(1)
    for i in range(0, n):
        connec, addr = sockobj.accept()
        clients.append(connec)
        thread = threading.Thread(target = secretqs, args = (clients[i],))
        thread.start()
    sockobj.close()

if __name__ == '__main__':
    main()

