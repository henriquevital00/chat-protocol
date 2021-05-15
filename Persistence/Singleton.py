from peewee import SqliteDatabase


class Singleton:

    _instance = None

    @staticmethod
    def instance():
        if not Singleton._instance:
            Singleton._instance SqliteDatabase('Persistence/chat.db')
        return Singleton._instance
