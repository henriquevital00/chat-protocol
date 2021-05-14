from Persistence.DbContext import DbContext
from Persistence.Migrations.created_tables import  CreatedTableMigration
from Resources.UserResources import UserResources

def runMigrations():
    CreatedTableMigration().migrate()
    pass

def main():
    DbContext().get_conn()
    runMigrations()

if __name__ == '__main__':
    main()