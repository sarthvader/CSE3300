from socket import *
import random
import struct

serverName = 'tao.uits.uconn.edu'
serverPort = 3300
clientSocket = socket(AF_INET, SOCK_DGRAM)

# message struc
msgServer = 00110011100100
msgType = 0
msgRequestFlag = 0
msgLabNum = 0000
msgVersion = 0111

requestData = input('Enter your SSN:')
print ('Your SSN is '), requestData

checkSum = 0
clientCookie = random.randint(10000000,80000000)
result = 0

message = struct.pack('!2H2I2H', msgType, msgRequestFlag, msgServer, msgLabNum, clientCookie, requestData, checkSum, result)

print(message)
