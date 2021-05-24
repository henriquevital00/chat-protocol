from Commands.BaseCommand import BaseCommand

class Exit(BaseCommand):

    def __init__(self, client):
        super().__init__(client)

    def run(self, command):
        self.client.join()

        return 'Exit with success'
