#! /usr/bin/python

import socket


class Client:
    """Simple client to be used as an example
    with the server."""

    def __init__(self, hostname, port):
        self.host = hostname
        self.port = port

        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))

    def get_recv(self, buf):
        return self.socket.recv(buf)


client = Client('teenager', 9206)
print(client.get_recv(1024))
