from .Migration import Migration
from playhouse.migrate import migrate, SqliteMigrator
from peewee import TextField, ForeignKeyField
from Models.Room import Room

class AlterMessageTableMigration(Migration):

    def migrate(self):
        migrator = SqliteMigrator(self._conn)

        migrate(
            # migrator.add_column("message", 'file_name', TextField(null = True))
            migrator.add_column("message", "room_id", ForeignKeyField(Room, Room.id, null=True, default=None))
        )