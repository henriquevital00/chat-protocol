class Status():
    def __init__(self, status, body):
        self.status = status
        self.body = body


class Ok(Status):
    def __init__(self, body):
        super().__init__("OK!", body)

    def __new__(self, body):
        return body


class Alert(Status):
    def __init__(self, message):
        super().__init__("Alert!", message)

    def __new__(self, message):
        return Colors.OKBLUE + message + Colors.ENDC


class BadRequest(Status):
    def __init__(self, message):
        super().__init__("FAILED!", message)

    def __new__(self, message):
        return Colors.FAIL + message + Colors.ENDC


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
