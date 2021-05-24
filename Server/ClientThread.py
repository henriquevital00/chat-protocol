from Server.Check import Check
from Server.Session import Session

class ClientThread(Session):

    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    @staticmethod
    def connect(client, server):

        while True:
            try:
                message = client.conn.recv(2048).decode()

                if message:

                    result = Check.validateCommand(message, client) + '\n\n'

                    if client.activeRoom is not None and 'send' in message:
                        client.room_broadcast(result, server)
                    else:
                        client.conn.send(result.encode())

            except Exception as ex:
                print(ex)
                ex = str(ex) + '\n\n'
                client.conn.send(ex.encode())
                continue

            except KeyboardInterrupt as e:
                client.free_client(server)
                client.conn.close()

    def room_broadcast(self, message, server):

        for client in server.clients:

            if client.activeRoom == self.activeRoom:

                client.conn.send(message.encode())

    def free_client(self, server):

        if self.conn in server.clients:
            server.clients.remove(self.conn)


