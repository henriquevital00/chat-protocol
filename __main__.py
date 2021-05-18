from Persistence.DbContext import DbContext
from Persistence.Migrations.created_tables import CreatedTableMigration
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
    AccountController().signIn("testUser", "123")
    pmessages = MessageController().findPrivateMessages(1, 2)
    print(pmessages)
    for pm in pmessages:
        print(f'from_user => {pm}')
        print(f'to_user => {pm.to_user.username}')
        print(f'content => {pm.content}')

    
    #Server()

if __name__ == '__main__':
    main()