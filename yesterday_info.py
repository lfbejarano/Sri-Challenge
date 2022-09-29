from DataBase.Observation import observation
from DataBase.database import Database
from API.data_request import requester


def main():
    """
    Function to call api, request yesterday information AND
    insert it into the db
    """
    # class object to request data to the api
    api_request: requester = requester()
    records_to_insert = api_request.yesterday_weather_report()
    DB: Database = Database
    print('Initializing Database')
    DB.initialize_database()
    # class object observation to add to the database
    observ_class = observation(records_to_insert)
    # Saving records to the database
    observ_class.save_to_db()


if __name__ == "__main__":
    main()
