from socket import *
import random
import struct

serverName = 'tao.ite.uconn.edu'
serverPort = 3300
clientSocket = socket(AF_INET, SOCK_DGRAM)
timeout = 5.0
transmissionCount = 5

# message struc
msgServer = 3300
msgType = 0
msgRequestFlag = 0
msgLab = 4
msgVersion = 7
msgLabAndVersion = 0407 
requestData = input('Enter your SSN:')
print ('Your SSN is '), requestData

checkSum = 0
clientCookie = random.randint(10000000,80000000)
result = 0

message = struct.pack('!3H2I2H', msgServer, msgLab, msgVersion, clientCookie, requestData, checkSum, result)

print struct.unpack('!3H2I2H', message)

while(transmissionCount > 0):
    clientSocket.sendto(message, (serverName, serverPort))
    clientSocket.settimeout(timeout)
    responseMessage, serverAddress = clientSocket.recvfrom(1024)
    print ('Server Response: '), struct.unpack('!3H2I3H', responseMessage)
    if socket.timeout:
        print ('Timeout count = 1. Sending again')
        transmissionCount-=1


