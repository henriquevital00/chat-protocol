from Persistence.DbContext import DbContext
from Persistence.Migrations.created_tables import CreatedTableMigration
from Persistence.Migrations.drop_file_columns import DropFilesColumnsMigration
from Controllers.RoomController import RoomController
from Controllers.MessageController import MessageController
from Controllers.AccountController import AccountController
from Server.Server import Server
from Auth.Auth import Auth

def runMigrations():
    CreatedTableMigration().migrate()

def main():
    DbContext().get_conn()
    runMigrations()

    Server()

if __name__ == '__main__':
    main()