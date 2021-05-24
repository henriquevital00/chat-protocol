from socket import *
import _thread
from Server.Check import Check
from Controllers.RoomController import RoomController
from Controllers.AccountController import AccountController
from Controllers.UserController import UserController
from Controllers.MessageController import MessageController
import re

import threading

print_lock = threading.Lock()


class Server:

    clients = []

    def __init__(self):

        HOST, PORT = ('localhost', 8001)

        with socket(AF_INET, SOCK_STREAM) as sock:

            sock.bind((HOST, PORT))
            sock.listen(5)
            print("Listening at {}:{}".format(HOST, PORT))

            while True:
                conn, addr = sock.accept()

                newClient = ClientThread(conn, addr)
                self.clients.append(newClient)

                _thread.start_new_thread(ClientThread.connect,
                                         (newClient, self))


class Client():
    def __init__(self):

        self.accountData = None
        self.isLoggedIn = False
        self.activeRoom = None

        # Controllers
        self.roomController = RoomController(self)
        self.messageController = MessageController(self)
        self.accountController = AccountController(self)
        self.userController = UserController(self)


class ClientThread(Client):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    @staticmethod
    def connect(client, server):

        while True:
            try:
                originalMessage = client.conn.recv(2048).decode()

                if originalMessage:
                    message = Check.validateCommand(
                        re.sub(r'\r\n', '', originalMessage), client) + '\n\n'

                    if client.activeRoom is not None and 'send' in originalMessage:
                        client.broadcast(message, server)
                    else:
                        client.conn.send(message.encode())
                else:
                    client.remove(server)
            except Exception as ex:
                print(ex)
                ex = str(ex) + '\n\n'
                client.conn.send(ex.encode())
                continue
            except KeyboardInterrupt as e:
                client.remove(server)
                client.conn.close()

    def broadcast(self, message, server):

        for client in server.clients:

            if client.activeRoom == self.activeRoom:

                client.conn.send(message.encode())

    def remove(self, server):

        if self.conn in server.clients:
            server.clients.remove(self.conn)
