from peewee import SqliteDatabase

class DbContext:

    _conn = None

    def get_conn(self):
        try:

            if self._conn == None:
                self._conn = SqliteDatabase('Persistence/chat.db')
                self._conn.connect()

            return self._conn

        except Exception as ex:
            print(ex)

    def close_conn(self):
        self._conn.close()

