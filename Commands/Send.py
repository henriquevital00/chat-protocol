from Commands.BaseCommand import BaseCommand

class Send(BaseCommand):

    def __init__(self, client):
        super().__init__(client)

    def sendMessage(self, message):
        return self.client.messageController.saveMessage(message)

    def run(self, command):

        command = command.partition(' -m ')

        substr_command = command[0].split()

        message_content = substr_command[2].strip('"')

        return self.sendMessage(message_content)
