import socket


class Server:
    """Example game server class. Will contain
    database utilities, player tracking, etc."""

    def __init__(self, port):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = port
        self._s.bind((self.host, self.port))
        self.run()

    def run(self):
        s = self._s
        s.listen(5)
        while True:
            c, addr = s.accept()
            print('New connection from: {}'.format(addr))
            c.send('Welcome to {0}'.format(self.host).encode())

server = Server(9206)

