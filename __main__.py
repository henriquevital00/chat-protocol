from Persistence.DbContext import DbContext
from Persistence.Migrations.alter_message_table import AlterMessageTableMigration

from Resources.RoomResources import RoomResources
from Server import Server

def runMigrations():

    # CreatedTableMigration().migrate()
    # AssociativeEntitiesMigration().migrate()
    # AlterRoomTableMigration().migrate()
    #AlterMessageTableMigration().migrate()
    pass

def main():
    DbContext().get_conn()
    runMigrations()
    RoomResources().findRoomMessages(1)
    Server()

if __name__ == '__main__':
    main()