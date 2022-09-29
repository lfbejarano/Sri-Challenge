from DataBase.Observation import observation
from DataBase.database import Database
from API.data_request import requester


def main():
    """
    Function to call api, request custom information  based on
    start and end date AND insert it into the db
    """
    # class object to request data to the api
    api_request: requester = requester()
    DB: Database = Database
    print('please insert start date to retrieve info')
    print('Format must be: "%Y-%m-%dT%H:%M:%SZ"')
    start = input()
    print('please insert final date to retrieve info')
    print('Format must be: "%Y-%m-%dT%H:%M:%SZ"')
    stop = input()
    records_to_insert = api_request.get_weather_report(start, stop)
    print('Initializing Database')
    DB.initialize_database()
    # class object observation to add to the database
    observ_class = observation(records_to_insert)
    # Saving records to the database
    observ_class.save_to_db()


if __name__ == "__main__":
    main()
