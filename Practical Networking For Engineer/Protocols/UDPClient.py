from socket import *
serverName = '192.168.1.20'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = str(input("Input lowercase sentence: "))
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    
clientSocket.close()
