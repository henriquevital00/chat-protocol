from .Migration import Migration
from playhouse.migrate import migrate, SqliteMigrator

class DropFilesColumnsMigration(Migration):

    def migrate(self):
        migrator = SqliteMigrator(self._conn)

        migrate(
            migrator.drop_column("message", "file_name"),
            migrator.drop_column("message", "file")
        )