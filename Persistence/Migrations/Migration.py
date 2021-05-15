from abc import ABC, abstractmethod
from ..DbContext import DbContext

class Migration(ABC):

    _conn = DbContext.get_conn()

    def migrate(self):
        pass

