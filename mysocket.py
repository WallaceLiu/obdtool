import socket

class mysocket(object):
    """
        Python Class for connecting  tcp server.
    """

    __host = None
    __port = None
    __address = None
    __s = None

    def __init__(self, host='10.1.7.57', port=11000):
        self.__host = host
        self.__port = port
        self.__address = (self.__host, self.__port)  
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    ## End def __init__

    def connect(self):
        try:
            self.__s.connect(self.__address)
        except  Exception as e:
            print(e.args)

    def send(self, msg):
        self.__s.send(msg)
    ## End def send

    def close(self):
        self.__s.close()
    ## End def close
## End class