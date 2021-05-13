from peewee import SqliteDatabase

class DbContext:

    _conn = None

    def get_conn(self):
        try:

            if self._conn == None:
                self._conn = SqliteDatabase('chat.db')

            return self._conn

        except Exception as ex:
            print(ex)