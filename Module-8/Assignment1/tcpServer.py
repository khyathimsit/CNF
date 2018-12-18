import socket

def convert(data):
    tokens = data.split(" ")
    if (tokens[1] == "INR") :
        convert = int(tokens[2])/67
    if (tokens[1] == "Yen") :
        convert = int(tokens[2])/113.47
    if (tokens[1] == "Pound") :
        convert = int(tokens[2])/0.75
    if (tokens[1] == "Dollar"):
        if(tokens[0] == "INR"):
            convert = int(tokens[2])*67
        if(tokens[0] == "Yen"):
            convert = int(tokens[2])*113.47
        if(tokens[0] == "Pound"):
            convert = int(tokens[2])*0.75
    return convert
    
def main():
    host  = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    c, addr = s.accept()
    print ('connection from : '+ str(addr))
    while True :
        data = c.recv(1024)
        data = data.decode()
        if not data:
            break
        print ("from connected user : "+ str(data))
        data = str(data)
        currency = convert(data)
        print('encoding:'+ str(currency))
        c.send(str(currency).encode())
    c.close()

if __name__ == '__main__':
    main()
