from socket import *
import struct
import urllib2
import random

db = urllib2.urlopen('http://engr.uconn.edu/%7Esong/classes/cn/db').read()
db = db.split('\n')

serverIP = gethostbyname('tao.ite.uconn.edu')
serverPort = random.randint(1, 90000)
serverSocket = socket(AF_INET, SOCK_DGRAM)

head = 19684
labAndVersionNum = 1031

while 1:
    data, clientAddress = serverSocket.recvfrom(1024)
    message = struct.unpack('!2H2I2H', data)
    msgType = 1
    data = struc.pack('2H2I2H', head, labAndVersionNumber, message[2], message[3], 32769)
    serverSocket.send(data, clientAddress)
