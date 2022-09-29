from DataBase.database import Database


def main():
    """
    Function to be called to create the table
    """
    DB: Database = Database
    print('Initializing Database')
    DB.initialize_database()
    print('Creating Table if not exist')
    DB.create_table()


if __name__ == "__main__":
    main()
