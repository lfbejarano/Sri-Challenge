from psycopg2 import pool
from config import database, user, password, host


class Database:
    """
    Class that define connection pool for the database to recycle
    connections
    """
    __connection_pool = None
    #########################################################################

    @staticmethod
    def initialise(**kwargs):
        Database.__connection_pool = pool.SimpleConnectionPool(1, 2, **kwargs)

    @staticmethod
    def get_connection():
        return Database.__connection_pool.getconn()

    @staticmethod
    def return_connection(connection):
        Database.__connection_pool.putconn(connection)

    @staticmethod
    def close_all_connections():
        Database.__connection_pool.closeall()
    #########################################################################

    def initialize_database():
        "Initializing postgresql"
        Database.initialise(database=database, user=user,
                            password=password, host=host)

    def create_table():
        "Method to create  Observations table"
        with CursorFromConnectionPool() as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS Observations \
                        	(timestamp TIMESTAMP PRIMARY KEY NOT NULL, \
                        	temperature float default NULL); \
                            CREATE INDEX datetime_index \
                            ON Observations ((timestamp::DATE));')


class CursorFromConnectionPool:
    """
    cursor to manage all instructions for
    the Database and return the connection to the pool once is done
    """

    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = Database.get_connection()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value:  # This is equivalent to `if exception_value is not None`
            self.conn.rollback()
        else:
            self.cursor.close()
            self.conn.commit()
        Database.return_connection(self.conn)
