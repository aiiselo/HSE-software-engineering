import psycopg2 as ps
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class Database(object):
    def __init__(self, name):
        self.dbname = name
        self.user = 'myuser'
        self.password = 'mypass'
        self.host = 'localhost'
        self.port = '5432'
        self.connectDB()

    def connectDB(self):
        self.connection = ps.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()
        self.cursor.callproc("create db", (self.dbname, self.user))

    def create_database(self):
        self.cursor.callproc("Create database")

    def get_publishers(self):
        self.cursor.callproc("")