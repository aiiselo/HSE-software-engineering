from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog

import design
from PyQt5 import QtWidgets
from database import Database
import connectWindow


class connectWin(QtWidgets, connectWindow.Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi( self )
        self.app = app
        self.connect_button.clicked.connect(self.connect_to_database)

    def connect_to_database(self):
        try:
            self.app.connect(self.database_name)
            self.close()
        except Exception as ex:
            self.app.message("There is no such database!", str(ex))
            self.close()


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_to_book_button.clicked.connect(self.add_book_record)
        self.add_to_publisher_button.clicked.connect(self.add_publisher_record)
        self.clear_book_button.clicked.connect(self.clear_book)
        self.clear_publisher_button.clicked.connect(self.clear_publisher)
        self.delete_button.clicked.connect(self.delete_by_author)
        self.delete_database_button.clicked.connect(self.delete_database)
        self.clear_all.clicked.connect(self.clear_database)
        self.actionNew.triggered.connect(self.create_new_database)
        self.actionOpen.triggered.connect(self.open_database)
        self.actionSave.triggered.connect(self.save_database)
        self.tableWidget.itemChanged.connect(self.update_records)

    def connect(self, dbname):
        self.db = Database(dbname)
        self.db.connectDB()

    def message(self, error, detailed_error="¯\_(ツ)_/¯", icon=QMessageBox.Warning):
        msg = QMessageBox()
        msg.setWindowTitle("Отчёт")
        msg.setIcon(icon)
        msg.setText(f"{error}")
        msg.setDetailedText(detailed_error)
        msg.addButton(QMessageBox.Ok)
        msg.exec()

    def add_book_record(self):
        title = self.book_title
        author = self.book_author
        publisher = self.book_publisher

