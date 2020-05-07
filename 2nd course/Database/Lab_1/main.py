from gui import App
from PyQt5 import QtWidgets
import sys
from Book import DB


def main():
    app = QtWidgets.QApplication( sys.argv )
    window = App()
    window.show()
    app.exec_()
    # Books = DB("book")
    # Books.add_record("1", {"id":"1", "title":"Alice", "author":"Carol", "year":"1945", "price": "134"})
    # Books.add_record( "2", {"id": "2", "title": "Alice2", "author": "Carol2", "year": "1947", "price": "138"} )
    # print(Books.table)
    # print(Books.field)
    # Books.save_db("/Users/olesyamartinyuk/PycharmProjects/database/booksdb.json")
    # print(Books.directory)
    # Books.to_csv("/Users/olesyamartinyuk/PycharmProjects/database/booksdb.json")
    # Books.back_up("/Users/olesyamartinyuk/PycharmProjects/database/booksdb.json")
    # Books.deback_up("/Users/olesyamartinyuk/PycharmProjects/database/booksdb_backup.csv")
    # print(Books.table)
    # print(Books.field)
    # Books.save_db("/Users/olesyamartinyuk/PycharmProjects/database/booksdb.json")



if __name__ == '__main__':
    main()
