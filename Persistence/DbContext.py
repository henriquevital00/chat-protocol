from peewee import SqliteDatabase

class DbContext:

    _conn = None

    @staticmethod
    def get_conn():
        try:

            if DbContext._conn == None:
                DbContext._conn = SqliteDatabase('Persistence/chat.db')
                DbContext._conn.connect()

            return DbContext._conn

        except Exception as ex:
            print(ex)

    def close_conn(self):
        DbContext._conn.close()
