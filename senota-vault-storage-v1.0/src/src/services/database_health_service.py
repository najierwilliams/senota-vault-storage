from src.db.database import db
class DatabaseHealthService:
    def check(self):
        return db.connect()
