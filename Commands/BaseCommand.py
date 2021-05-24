from abc import ABC, abstractmethod

class BaseCommand(ABC):

    def __init__(self, client):
        self.client = client

    @abstractmethod
    def run(self, command):
        pass
