import socket
class host:
    def __init__(self):
        pass
    #host와 ip출력
    def hostnameandip(self):
        self.host_name= socket.gethostname()
        print(self.host_name)
        print(socket.gethostbyname(self.host_name))



