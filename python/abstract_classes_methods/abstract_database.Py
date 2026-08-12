#abstract class Database with an abstract method connect(). Implement it using MySQLDatabase and PostgreSQLDatabase.
from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL database.")
class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL database.")
MySQLDatabase().connect()
PostgreSQLDatabase().connect()