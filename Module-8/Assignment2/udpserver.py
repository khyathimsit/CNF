import socket
def main():
    host = '127.0.0.1'
    port = 5000
    dict = {"INRTODollar" : 0.0149,"DollarTOINR" : 67, "DollarTOPounds" : 0.75, "PoundsTODollar" : 1.3333, "DollarTOYen" : 113.41, "YenTODollar" : 0.0088}
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print('server started.')
    while True:
        data, addr = s.recvfrom(1024)
        print('message from : '+ str(addr))
        print('from connect user : '+ str(data))
        data = data.decode()
        data = data.split(" ")
        result = int(data[2])*(dict[data[1]+data[3]+data[4]])
        result = round(result, 1)
        print('sending : '+ str(result))
        s.sendto(str(result).encode(),addr)
    s.close()

if __name__ == '__main__':
    main()