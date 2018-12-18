import socket
def main():
    host  = '127.0.0.1'
    port = 5000
    dict = {"INRTODollar" : 0.0149,"DollarTOINR" : 67, "DollarTOPounds" : 0.75, 
            "PoundsTODollar" : 1.3333, "DollarTOYen" : 113.41, "YenTODollar" : 0.0088}
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    c, addr = s.accept()
    print ('connection from : '+ str(addr))
    while True :
        data = c.recv(1024).decode()
        if not data:
            break
        print ("from connected user : "+ str(data))
        data = data.split(" ")
        # if(list1[1] == 'INR' and list1[4] == 'Dollar'):
        #   result = int(list1[2])/67
        # elif(list1[1] == 'Dollar' and list1[4] == 'Pounds'):
        #   result = int(list1[2])*0.75
        result = int(data[2])*(dict[data[1]+data[3]+data[4]])
        result = round(result, 1)
        print('sending: '+ str(result))
        c.send(str(result).encode())
    c.close()

if __name__ == '__main__':
    main()
