from socket import *
import random

ipLocal = gethostbyname(gethostname())

serverName = 'tao.ite.uconn.edu'
serverPort = 3300

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

usernum = random.randint(1000, 8000)
requestString = 'ex0 137.99.3.212-%s %s %s S.Bhatnagar\n' %(serverPort, ipLocal, usernum)
print requestString
clientSocket.send(requestString)

modifiedString = clientSocket.recv(1024)
if not(modifiedString.find('OK')):
       print 'No OK'
print 'From Server: %s' %(modifiedString)   

clientSocket.close()



               
