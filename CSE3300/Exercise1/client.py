from socket import *
import random

serverName = 'tao.ite.uconn.edu'
serverPort = 3300
#localIP = gethostbyname(gethostname())                                                    
usernum = random.randint(1000, 8000)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

psock = socket(AF_INET, SOCK_STREAM)
psock.bind(('', 0))
localPort = psock.getsockname()[1]
#print 'Local IP : ', localIP                                                              
print 'Port : ', localPort
psock.listen(5)

requestString = 'ex1 137.99.37.212-3300 137.99.82.172-%s %s S.Bhatnagar\n' %( localPort, u\
sernum)
print requestString
clientSocket.send(requestString)
modifiedString = clientSocket.recv(1024)
print 'From Server: ', modifiedString

#if (modifiedString.find('OK') != -1):                                                     
servernumIndex = modifiedString.find('gar')
servernum = int(modifiedString[servernumIndex + 4: servernumIndex + 14])
newsock, newsockAddress = psock.accept()
serverResponse = newsock.recv(1024)

newservernumIndex = serverResponse.find('calling')
newservernum = int(serverResponse[newservernumIndex + 8:])
print 'CSE 3300 server sent', newservernum
newrequestString = '%s %s \n' %(servernum + 1 , newservernum + 1)
newsock.send(newrequestString)
newsock.close()

data = clientSocket.recv(1024)
print data

clientSocket.close()
