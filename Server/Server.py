from socket import *
import _thread
from Server.ClientThread import *

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

                _thread.start_new_thread(ClientThread.connect,(newClient, self))