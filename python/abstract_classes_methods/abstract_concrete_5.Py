#abstract Database class with an abstract method connect() and a normal method display_database_name().
from abc import ABC, abstractmethod
class Database(ABC):
    def display_database_name(self):
        print("This is a database.")

    @abstractmethod
    def connect(self):
        pass
class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL database.")
class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL database.")
MySQLDatabase().display_database_name()
MySQLDatabase().connect()
PostgreSQLDatabase().display_database_name()
PostgreSQLDatabase().connect()