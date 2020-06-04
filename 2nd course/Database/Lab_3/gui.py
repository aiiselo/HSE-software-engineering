import traceback
import design
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from database import Database
import connectWindow


class connectWin(QtWidgets.QMainWindow, connectWindow.Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.connect_button.clicked.connect(self.connect_to_database)

    def connect_to_database(self):
        try:
            self.app.connect(self.database_name.text())
            self.close()
        except Exception as ex:
            print(traceback.format_exc())
            self.message("There is no such database!", traceback.format_exc())


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.db = None
        self.setupUi(self)
        self.connectionWindow = connectWin(self)
        self.add_to_book_button.clicked.connect(self.add_book_record)  #
        self.add_to_publisher_button.clicked.connect(self.add_publisher_record)  #
        self.clear_book_button.clicked.connect(self.clear_book)  #
        self.clear_publisher_button.clicked.connect(self.clear_publisher)  #
        self.delete_button.clicked.connect(self.delete_by_author)  #
        self.delete_database_button.clicked.connect(self.delete_database)  #
        self.search_button.clicked.connect(self.search_by_author)
        self.clear_all.clicked.connect(self.clear_database)
        self.actionOpen.triggered.connect(self.connectionWindow.show)
        self.actionDelete.triggered.connect(self.delete_record)
        self.columns_publishers = ['name', 'telephone', 'lastUpdate']
        self.columns_books = ['id', 'title', 'author', 'publisher']
        self.book_table.itemChanged.connect(self.update_books)
        self.publisher_table.itemChanged.connect(self.update_publishers)
        self.book_table.setColumnCount(4)
        self.publisher_table.setColumnCount(3)
        self.book_table.setHorizontalHeaderLabels(self.columns_books)
        self.publisher_table.setHorizontalHeaderLabels(self.columns_publishers)
        self.edit_flag = False

    def connect(self, dbname):
        self.db = Database(dbname)
        try:
            self.data_books = self.db.get_books()
            self.data_publishers = self.db.get_publishers()
            self.set_data(self.book_table, self.columns_books, self.data_books)
            self.set_data(self.publisher_table, self.columns_publishers, self.data_publishers)
        except Exception as ex:
            print(traceback.format_exc())
            self.message("Error during connect!", traceback.format_exc())

    def set_data(self, table, columns, data):
        self.edit_flag = True
        try:
            if data is not None:
                table.setRowCount(len(data))
                for i, row in enumerate(data):
                    for j, col in enumerate(columns):
                        table.setItem(i, j, QTableWidgetItem(str(row[col])))

            else:
                table.setRowCount(0)
        except Exception as ex:
            self.message("Error during setting data!", traceback.format_exc())
        self.edit_flag = False

    def message(self, error, detailed_error="¯\_(ツ)_/¯", icon=QMessageBox.Warning):
        msg = QMessageBox()
        msg.setWindowTitle("Отчёт")
        msg.setIcon(icon)
        msg.setText(f"{error}")
        msg.setDetailedText(detailed_error)
        msg.addButton(QMessageBox.Ok)
        msg.exec()

    def add_book_record(self):
        try:
            title = self.book_title.text()
            author = self.book_author.text()
            publisher = self.book_publisher.text()
            if title != "" and author != "" and publisher != "" and self.db is not None:
                self.db.add_to_book(title, author, publisher)
                self.data_books = self.db.get_books()
                self.set_data(self.book_table, self.columns_books, self.data_books)
                self.book_title.clear()
                self.book_author.clear()
                self.book_publisher.clear()
            else:
                self.message(
                    "Check if all fields (title, author, publisher) are filled or if you have connected to db")
        except Exception as ex:
            self.message("Error during additing data!", traceback.format_exc())

    def add_publisher_record(self):
        try:
            name = self.publisher_name.text()
            telephone = self.publisher_telephone.text()
            if name != "" and telephone != "" and self.db is not None:
                self.db.add_to_publisher(name, telephone)
                self.data_publishers = self.db.get_publishers()
                self.set_data(self.publisher_table, self.columns_publishers, self.data_publishers)
                self.publisher_name.clear()
                self.publisher_telephone.clear()
            else:
                self.message("Check if all fields (name, telephone) are filled or if you have connected to db")

        except Exception as ex:
            print(traceback.format_exc())
            self.message("Error during additing data!", str(ex))

    def clear_book(self):
        try:
            self.db.clear_books()
            self.data_books = self.db.get_books()
            self.set_data(self.book_table, self.columns_books, self.data_books)
        except Exception as ex:
            self.message("Error during clearing data!", traceback.format_exc())

    def clear_publisher(self):
        try:
            self.db.clear_publishers()
            self.data_publishers = self.db.get_publishers()
            self.set_data(self.publisher_table, self.columns_publishers, self.data_publishers)
        except Exception as ex:
            self.message("Error during clearing data!", traceback.format_exc())

    def clear_database(self):
        try:
            self.clear_book()
            self.clear_publisher()
        except Exception as ex:
            self.message("Error during clearing data!", traceback.format_exc())

    def delete_database(self):
        try:
            if self.db is not None:
                self.db.delete_database()
                self.data_publishers = []
                self.data_books = []
                self.set_data(self.publisher_table, self.columns_publishers, self.data_publishers)
                self.set_data(self.book_table, self.columns_books, self.data_books)
                self.db = None
                self.connectionWindow = None
                self.connectionWindow = connectWin(self)
            else:
                self.message("Check if you have connected to db")
        except Exception as ex:
            self.message("Error during deleting database!", traceback.format_exc())

    def delete_by_author(self):
        try:
            author = self.data_to_delete.text()
            if author != "" and self.db is not None:
                self.db.delete_book_by_author(author)
                self.data_books = self.db.get_books()
                self.set_data(self.book_table, self.columns_books, self.data_books)
                self.data_to_delete.clear()
            else:
                self.message("Check if all fields (author) are filled or if you have connected to db")
        except Exception as ex:
            self.message("Error during deleting data!", traceback.format_exc())

    def find_by_author(self):
        try:
            author = self.data_to_delete.text()
            if author != "" and self.db is not None:
                self.set_data(self.book_table, self.columns_books, self.db.find_book_by_author(author))
                self.set_data(self.publisher_table, self.columns_publishers, self.db.find_publisher(author))
                self.data_to_delete.clear()
            if author == "":
                self.set_data(self.book_table, self.columns_books, self.data_books)
                self.set_data(self.publisher_table, self.columns_publishers, self.data_publishers)
            else:
                self.message("Check if you have connected to db")
        except Exception as ex:
            self.message("Error during data search!", traceback.format_exc())

    def update_books(self, item):
        if not self.edit_flag:
            try:
                if item.column() == 1:
                    self.db.update_book_by_title(item.text(), self.book_table.item(item.row(), 0).text())
                elif item.column() == 2:
                    self.db.update_book_by_author(item.text(), self.book_table.item(item.row(), 0).text())
                elif item.column() == 3:
                    self.db.update_book_by_publisher(item.text(), self.book_table.item(item.row(), 0).text())
                self.data_books = self.db.get_books()
                self.set_data(self.book_table, self.columns_books, self.data_books)
            except Exception:
                self.message("Error during data update!", traceback.format_exc())

    def update_publishers(self, item):
        if not self.edit_flag:
            try:
                if item.column() == 0:
                    self.db.update_publisher_by_name(item.text(), self.data_publishers[item.row()]['name'])
                elif item.column() == 1:
                    self.db.update_publisher_by_tel(item.text(), self.publisher_table.item(item.row(), 0).text())
                self.data_publishers = self.db.get_publishers()
                self.set_data(self.publisher_table, self.columns_publishers, self.data_publishers)
            except Exception:
                print(traceback.format_exc())
                self.message("Error during data update!", traceback.format_exc())

    def search_by_author(self):
        try:
            author = self.data_to_delete.text()
            if author != "" and self.db is not None:
                self.set_data(self.book_table, self.columns_books, self.db.find_book_by_author(author))
                self.set_data(self.publisher_table, self.columns_publishers, self.db.find_publisher(author))
                self.data_to_delete.clear()
                self.data_to_delete.clear()
            else:
                self.set_data(self.book_table, self.columns_books, self.data_books)
                self.set_data(self.publisher_table, self.columns_publishers, self.data_publishers)
        except Exception:
            self.message("Error during data search!", traceback.format_exc())

    def delete_record(self):
        if len(self.publisher_table.selectedIndexes()):
            try:
                for i in self.publisher_table.selectedIndexes():
                    self.db.delete_publisher_record(self.data_publishers[i.row()]['name'])
                    self.data_publishers = self.db.get_publishers()
                    self.set_data(self.publisher_table, self.columns_publishers, self.data_publishers)
            except Exception:
                self.message("Error during data delete!", traceback.format_exc())
        else:
            try:
                for i in self.book_table.selectedIndexes():
                    self.db.delete_book_record(self.data_books[i.row()]['id'] )
                    self.data_books = self.db.get_books()
                    self.set_data(self.book_table, self.columns_books, self.data_books)
            except Exception:
                self.message("Error during data delete!", traceback.format_exc())