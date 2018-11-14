class mysocket:
    def _init_(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

     def connect(self, host, port):
         self.sock.connect((host, port))

         

               
