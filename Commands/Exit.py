class Exit:
    @staticmethod
    def run(command, client):
        client.join()
        return 'Exit with success'
