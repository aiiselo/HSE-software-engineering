import psycopg2 as ps
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Database(object):
    def __init__(self, name):
        self.dbname = name
        self.user = 'myuser'
        self.password = 'mypass'
        self.host = 'localhost'
        self.port = '5432'
        self.connectDB("postgres")
        self.cursor.execute("SELECT * FROM pg_catalog.pg_database WHERE datname = %s", (self.dbname,))
        flag = self.cursor.fetchone()
        if flag is None:
            self.cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self.dbname)))
        self.connection.close()
        self.connectDB(self.dbname)
        if flag is None:
            with self.connection as cursor_:
                cursor_.execute(open("commands.sql", "r").read())

    def connectDB(self, name):
        self.connection = ps.connect(
            dbname=name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.connection.set_isolation_level( ISOLATION_LEVEL_AUTOCOMMIT )
        self.cursor = self.connection.cursor()

    def delete_database(self):
        self.connectDB("postgres")
        self.cursor.execute(sql.SQL(f"DROP DATABASE {self.dbname}"))
        self.connection.close()
        del self

    def create_database(self):
        self.cursor.callproc("create_database")

    def get_publishers(self):
        self.cursor.callproc("get_publishers")
        return self.cursor.fetchone()[0]

    def get_books(self):
        self.cursor.callproc("get_books")
        return self.cursor.fetchone()[0]

    def add_to_publisher(self, name, telephone):
        self.cursor.callproc("add_to_publisher", (name, telephone,))

    def add_to_book(self, title, author, publisher):
        self.cursor.callproc("add_to_book", (title, author, publisher,))

    def clear_publishers(self):
        self.cursor.callproc("clear_publishers")

    def clear_books(self):
        self.cursor.callproc("clear_books")

    def clear_all(self):
        self.cursor.callproc("clear_all")

    def find_book_by_author(self, author):
        self.cursor.callproc("find_book", (author,))
        return self.cursor.fetchone()[0]

    def find_publisher(self, author):
        self.cursor.callproc("find_publisher", (author,))
        return self.cursor.fetchone()[0]

    def delete_book_by_author(self, author):
        self.cursor.callproc("delete_book_by_author", (author,))

    def delete_publisher_record(self, id):
        self.cursor.callproc("delete_publisher_record", (id,))

    def delete_book_record(self, id):
        self.cursor.callproc("delete_book_record", (id,))

    def update_publisher_by_name(self, newname, id):
        self.cursor.callproc("update_publisher_by_name", (newname, id,))

    def update_publisher_by_tel(self, newtel, id):
        self.cursor.callproc("update_publisher_by_tel", (newtel, id,))

    def update_book_by_title(self, newtitle, id):
        self.cursor.callproc("update_book_by_title", (newtitle, id,))

    def update_book_by_author(self, newauthor, id):
        self.cursor.callproc("update_book_by_author", (newauthor, id,))

    def update_book_by_publisher(self, newpubl, id):
        self.cursor.callproc("update_book_by_publisher", (newpubl, id,))

    def disconnect(self):
        self.connection.close()
