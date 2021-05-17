class Status():

    def __init__(self, status, body, color):
        self.status = status
        self.body = body
        self.color = color

class Ok(Status):

    def __init__(self, body):
        super().__init__("OK!", body, Colors.OKGREEN)

    def __new__(self, body):
        return body

class BadRequest(Status):

    def __init__(self, message):
        super().__init__("FAILED!", message, Colors.FAIL)

    def __new__(self, message):
        return self.color + message + Colors.ENDC


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'