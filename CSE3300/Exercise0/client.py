from socket import *
import random

#gets the computers IP address
ipLocal = gethostbyname(gethostname())

serverName = 'tao.ite.uconn.edu'
serverPort = 3300

#new socket and connecting to the given server name and server port
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

#generating a random number
usernum = random.randint(1000, 8000)

#constructing request string to send to server
requestString = 'ex0 137.99.3.212-%s %s %s S.Bhatnagar\n' %(serverPort, ipLocal, usernum)
print requestString
clientSocket.send(requestString)

#getting the reply from the server
modifiedString = clientSocket.recv(1024)
print 'From Server: ', modifiedString

#getting the servernum
servernumIndex = modifiedString.find('gar')
servernum = int(modifiedString[servernumIndex + 4 : ])

#checking if OK was in the recv. creating ackString with incremented usernum and servernum
if (modifiedString.find('OK') != -1):
   # newusernum = usernum+2
   # newservernum = servernum+1
    print 'found OK'
    ackString = 'ex0 %s %s\n' %((usernum+2), (servernum+1))
    print ackString
    clientSocket.send(ackString)
    serverAckString = clientSocket.recv(1024)
    print serverAckString
else:
    print 'Error No OK'
    print 'From server: %s' %(moddifiedString)
    
clientSocket.close()



               
