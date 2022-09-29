from DataBase.database import CursorFromConnectionPool
from datetime import datetime


class observation:
    def __init__(self, records: list = []) -> None:
        self.__records = records

    def __repr__(self):
        return print(self.records)

    def get_info_db(self) -> list:
        """
        Method that retrieves  Observation Table records
        """
        with CursorFromConnectionPool() as cursor:
            sql_prev_data = "SELECT * FROM Observations"
            cursor.execute(sql_prev_data)
            records = cursor.fetchall()
        return records

    def save_to_db(self) -> None:
        """
        Method that gets a connection from the pool and at the end returns it
        With the connection, it first queries the database to check if there is
        any record within the timeframe of the input, if so, deletes them and
        then insert the new records
        """
        try:
            start = datetime.strptime(
                self.__records[0][0], "%Y-%m-%dT%H:%M:%S+00:00")
            start = start.strftime("%Y-%m-%d %H:%M:%S")
            final = datetime.strptime(
                self.__records[-1][0], "%Y-%m-%dT%H:%M:%S+00:00")
            final = final.strftime("%Y-%m-%d %H:%M:%S")
        except IndexError:
            return print('No data Available for such interval')
        except ValueError:
            return print('Input does not match acceptable format')

        with CursorFromConnectionPool() as cursor:
            sql_prev_data = "SELECT * FROM Observations \
                            WHERE timestamp >= '" + start + \
                            "' AND timestamp <= '" + final + "'"
            cursor.execute(sql_prev_data)
            records = cursor.fetchall()
            if len(records) > 0:
                print('Found previous records and deleted them')
                delete_previous = "DELETE  FROM Observations \
                                WHERE timestamp >= '" + start + \
                    "' AND timestamp <= '" + final + "'"
                cursor.execute(delete_previous)
            else:
                pass

            args_str = ','.join(cursor.mogrify("(%s,%s)", x).decode('utf-8')
                                for x in self.__records)
            cursor.execute("INSERT INTO Observations VALUES " + args_str)
            print('{} records were inserted in the db'.format(len(self.__records)))
