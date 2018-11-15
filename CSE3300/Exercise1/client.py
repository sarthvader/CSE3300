from socket import *

serverName = 'tao.ite.uconn.edu'
serverPort = 3300

psock = socket(AF_INET, SOCK_STREAM)
psock.bind('', 0)

