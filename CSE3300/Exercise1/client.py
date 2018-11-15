from socket import *
import random

serverName = 'tao.ite.uconn.edu'
serverPort = 3300
localIP = gethostbyname(gethostname())
usernum = random.randint(1000, 8000)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

psock = socket(AF_INET, SOCK_STREAM)
psock.bind(('', 0))
localPort = psock.getsockname()[1]
print 'Local IP : ', localIP 
print 'Port : ', localPort
psock.listen(5)

requestString = 'ex1 137.99.3.212-3300 %s-%s %s S.Bhatnagar\n' %(localIP, localPort, usernum)
print requestString
clientSocket.send(requestString)
modifiedString = clientSocket.recv(1024)
print 'From Server: ', modifiedString

#if (modifiedString.find('OK') != -1):
#servernumIndex = modifiedString.find('gar') 
#servernum = int(modifiedString[servernumIndex + 4: servernumIndex + 14])

newsock = psock.accept()
serverResponse = newsock.recv(1024)

#newservernumIndex = serverResponse.find('gar')
#newservernum = int(serverResponse[newservernumIndex + 4: newservernumberIndex + 14])
#print 'CSE 3300 server sent ', newservernum
#newrequestString = '%s %s /n' %(servernum + 1, newservernum + 1)
#newsock.send(requestString)
#else:
  # print 'Error: No OK found'
   #clientSocket.close()
   
newsock.close()   
psock.close()
clientSocket.close()
