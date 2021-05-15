from Persistence.DbContext import DbContext
from Persistence.Migrations.created_associative_entities import  AssociativeEntitiesMigration
from Resources.UserResources import UserResources

def runMigrations():
    # CreatedTableMigration().migrate()
    AssociativeEntitiesMigration().migrate()

def main():
    DbContext().get_conn()
    runMigrations()

if __name__ == '__main__':
    main()