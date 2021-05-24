from abc import ABC


class BaseService(ABC):
    def __init__(self, client):
        self.client = client
