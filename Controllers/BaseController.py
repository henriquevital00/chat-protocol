from abc import ABC


class BaseController(ABC):
    def __init__(self, client):
        self.client = client
