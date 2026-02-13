from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self,data):
        pass

class MySQLDatabase(Database):
    def save(self,data):
        print("Saving data to MySQL")

class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving '{data}' to PostgreSQL Database")

class App:
    def __init__(self, db: Database):
        self.db = db

    def save_data(self, data):
        self.db.save(data)


