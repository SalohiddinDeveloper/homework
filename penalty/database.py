import pymysql

from config import database_config


class DatabaseManager:
    def __init__(self, db_config: dict) -> None:
        self.config = db_config
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = pymysql.connect(**self.config)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()

        if self.conn:
            self.conn.close()

        if self.cursor:
            self.cursor.close()

    def execute(self, query, params=None):
        self.cursor.execute(query, params)


def execute_query(query: str, params=None, fetch=None):
    with DatabaseManager(database_config) as db:
        try:
            db.execute(query=query, params=params)
            if fetch == "all":
                return db.cursor.fetchall()
            elif fetch == "one":
                return db.cursor.fetchone()
        except Exception as e:
            print(e)
