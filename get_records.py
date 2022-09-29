from DataBase.Observation import observation
from DataBase.database import Database


def main():
    """
    Function that gets all the records from observation table
    and print them
    """
    DB: Database = Database
    print('Initializing Database')
    DB.initialize_database()
    # class object observation to call the database
    observ_class: observation = observation()
    # Saving records to the database
    records = observ_class.get_info_db()
    print('timestamp temperature')
    for tuple in records:
        timestamp, temperature = tuple
        print(timestamp, temperature)


if __name__ == "__main__":
    main()
