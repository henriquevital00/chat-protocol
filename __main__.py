from Persistence.DbContext import DbContext
from Persistence.Migrations.alter_room_table import AlterRoomTableMigration
from Resources.UserResources import UserResources

def runMigrations():

    # CreatedTableMigration().migrate()
    # AssociativeEntitiesMigration().migrate()
    # AlterRoomTableMigration().migrate()
    # AlterMessageTableMigration().migrate()
    pass

def main():
    DbContext().get_conn()
    runMigrations()

if __name__ == '__main__':
    main()