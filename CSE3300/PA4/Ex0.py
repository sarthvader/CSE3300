from socket import *
import random
import struct

serverName = 'tao.ite.uconn.edu'
serverIP = gethostbyname(serverName)
serverPort = 3301
clientSocket = socket(AF_INET, SOCK_DGRAM)
timeout = 5.0
transmissionCount = 5
timeoutCount = 0

# message struc
msgServer = 3300
msgType = 0
msgRequestFlag = 0
msgLab = 4 #0100
msgVersion = 7 #0111
msgLabAndVersion = 1031
requestData = input('Enter your SSN:')
print ('Your SSN is '), requestData

checkSum = 0
clientCookie = random.randint(10000000,80000000)
result = 0

message = struct.pack('!2H2I2H', msgServer, msgLabAndVersion, clientCookie, requestData, checkSum, result)

print struct.unpack('!2H2I2H', message)

while(transmissionCount > 0):
    clientSocket.sendto(message, (serverIP, serverPort))
    try:
        clientSocket.settimeout(timeout)
        responseMessage, serverAddress = clientSocket.recvfrom(1024)
        print ('Server Response: '), struct.unpack('!2H2I2H', responseMessage)
        
    except timeout:
        print ('Timeout. Sending again')
        timeoutCount += 1
    transmissionCount -= 1
    if (transmissionCount < 5):
        break

