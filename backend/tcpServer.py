import socket, threading
import time

import tcpServerThread

class TCPServer(threading.Thread):
    def __init__(self, commandQueue, HOST, PORT):
        threading.Thread.__init__(self)

        self.commandQueue = commandQueue
        self.HOST = HOST
        self.PORT = PORT

        self.connections = []
        self.tcpServerThreads = []

    def run(self):
        try:
            while True:
                self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.serverSocket.bind(('', self.PORT))
                self.serverSocket.listen(1)

                print('tcp server :: server wait...')
                connection, clientAddress = self.serverSocket.accept()
                print("connect!")
                self.connections.append(connection)
                print("tcp server :: connect :", clientAddress)

                subThread = tcpServerThread.TCPServerThread(self.commandQueue, self.tcpServerThreads, self.connections,
                                                            connection, clientAddress)
                subThread.start()
                self.tcpServerThreads.append(subThread)
                self.serverSocket.close()
        except:
            print("tcp server :: serverThread error")

    def sendAll(self, message):
        try:
            self.tcpServerThreads[0].send(message)
        except:
            pass
