from .Migration import Migration
from playhouse.migrate import migrate, SqliteMigrator
from peewee import  BooleanField
from Models.User import User

class AlterRoomTableMigration(Migration):

    def migrate(self):
        migrator = SqliteMigrator(self._conn)

        migrate(
            # migrator.add_column("room", 'admin', ForeignKeyField(User, User.id, null=True)),
            # migrator.add_column("roomuser", "isInRoom", BooleanField(default=False))
            migrator.drop_column("room", "is_public")
        )

