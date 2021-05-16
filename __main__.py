from Persistence.DbContext import DbContext
from Persistence.Migrations.created_tables import CreatedTableMigration
from Resources.RoomResources import RoomResources
from Server.Server import Server

def runMigrations():
    CreatedTableMigration().migrate()

def main():
    DbContext().get_conn()
    runMigrations()
    RoomResources().findRoomMessages(1)
    Server()

if __name__ == '__main__':
    main()