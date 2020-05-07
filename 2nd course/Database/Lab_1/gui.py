from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog

import design
from PyQt5 import QtWidgets
from Book import DB


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        self.db = DB("book")
        super().__init__()
        self.setupUi(self)
        self.button_add.clicked.connect(self.add_new_record)
        self.button_delete.clicked.connect(self.delete_record)
        self.button_backup.clicked.connect(self.create_backup)
        self.button_export.clicked.connect(self.export)
        self.button_import.clicked.connect(self.import_from_csv)
        self.button_delete_db.clicked.connect(self.delete_db)
        self.button_recover.clicked.connect(self.debackup)
        self.tableWidget.itemChanged.connect(self.update_record)
        self.actionOpen.triggered.connect(self.load_fileinfo)
        self.actionSave.triggered.connect(self.save_changes)
        self.columns = ['id', 'title', 'author', 'year', 'price']
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(self.columns)
        self.changed = False
        self.able_to_edit = False

    def add_new_record(self):
        id = self.id.text()
        title = self.title.text()
        author = self.author.text()
        year = self.year.text()
        price = self.price.text()
        if id.isnumeric() and title and author and year.isnumeric() and price.isnumeric():
            try:
                self.db.add_record(id, {"id": id, "title": title, "author": author, "year": year, "price": price})
            except Exception as ex:
                self.message(f"{self.db.table[id]} already exists!", detailed_error=str(ex))
            self.id.clear()
            self.title.clear()
            self.author.clear()
            self.year.clear()
            self.price.clear()
        else:
            self.message("Please check if fields are filled in correctly",
                         "ID, Year, Price - numeric\nAuthor - string")
        self.show_data(self.db.get_table_records())
        self.changed = True

    def delete_record(self):
        searchInfo = self.data_search.text()
        try:
            if searchInfo in self.db.table.keys():
                reply = QMessageBox.question(self, 'ID is found!', f'An entry with such ID has been found = {searchInfo}. Delete?',
                                             QMessageBox.No, QMessageBox.Yes)
                if not reply: return
                if reply == QMessageBox.Yes:
                    self.db.delete_by_book_id(searchInfo)
            if searchInfo in self.db.field.keys():
                self.db.delete_by_field(searchInfo)
            self.show_data(self.db.get_table_records())
            self.changed = True
            self.data_search.clear()
        except Exception as ex:
            self.message("No information has been found for this request", str(ex))

    def show_data(self, data):
        self.able_to_edit = False
        self.db_data = data
        self.tableWidget.setRowCount(len(data))
        for rownum, row in enumerate(data):
            for colnum, col in enumerate(self.columns):
                self.tableWidget.setItem(rownum, colnum, QTableWidgetItem( str( row[col] ) ) )
        self.able_to_edit = True

    def save_changes(self):
        if self.db.directory != "":
            fname = self.db.directory
        else:
            fname = QFileDialog.getSaveFileName(self, 'Save file', '', 'json(*.json)')[0]
        try:
            self.db.save_db(fname)
        except Exception as ex:
            self.message("Error during saving", str(ex))
            return
        self.changed = False

    def check_before_save(self, quit_msg):
        reply = QMessageBox.question( self, 'Save?',
                                          quit_msg, QMessageBox.No, QMessageBox.Yes )
        if reply == QMessageBox.Yes:
            self.save_changes()
        return True

    def closeEvent(self, event):
        if self.changed == True:
            if self.check_before_save("Save changes?"):
                event.accept()
            else:
                event.ignore()

    def load_fileinfo(self):
        if self.changed:
            self.check_before_save("Save changes?")
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'json(*.json)')[0]
        if not fname: return
        try:
            self.db.get_info_from_file(fname)
            self.db.directory = fname
            self.show_data(self.db.get_table_records())
        except Exception as ex:
            self.message("Error during opening", str(ex))
            return

    def message(self, error, detailed_error="¯\_(ツ)_/¯", icon=QMessageBox.Warning):
        msg = QMessageBox()
        msg.setWindowTitle("Отчёт")
        msg.setIcon(icon)
        msg.setText(f"{error}")
        msg.setDetailedText(detailed_error)
        msg.addButton(QMessageBox.Ok)
        msg.exec()

    def create_backup(self):
        fname = QFileDialog.getSaveFileName(self, 'Save file', '', 'csv(*.csv)')[0]
        if not fname: return
        try:
            self.db.back_up(fname)
            self.message( error="Back-up file has been created", detailed_error=fname, icon=QMessageBox.Information)
        except Exception as ex:
            self.message(error="Error during operation", detailed_error=str(ex))

    def export(self):
        fname = QFileDialog.getSaveFileName(self, 'Save file', '', 'csv(*.csv)')[0]
        if not fname: return
        try:
            self.db.to_csv(fname)
            self.message( error="The file was exported", detailed_error=fname, icon=QMessageBox.Information)
        except Exception as ex:
            self.message(error="Error during file exporting ", detailed_error=str(ex))

    def import_from_csv(self):
        if self.changed:
            self.check_before_save("Save changes?")
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', f'csv(*.csv)')[0]
        if not fname: return
        try:
            self.db.deback_up(fname)
        except Exception as ex:
            self.message(error="Error during file loading", detailed_error=str(ex))
        self.show_data(self.db.get_table_records())

    def delete_db(self):
        reply = QMessageBox.question(self, 'Delete?',
                    f'Do you really want to delete this {self.db.name} database?', QMessageBox.No, QMessageBox.Yes)
        if not reply: return
        if reply == QMessageBox.Yes:
            self.db.clear_db()
            self.db.delete_db(self.db.directory)
            self.show_data(self.db.get_table_records())
        else:
            pass

    def debackup(self):
        if self.changed:
            self.check_before_save("Save changes?")
        fname = QFileDialog.getOpenFileName( self, 'Open file', '', f'csv(*_backup.csv)' )[0]
        if not fname: return
        try:
            self.db.deback_up(fname)
        except Exception as ex:
            self.message(error="Error during file loading", detailed_error=str(ex))
        self.show_data(self.db.get_table_records())

    def update_record(self, item):
        if self.able_to_edit:
            try:
                update = self.db_data[item.row()].copy()
                id = update['id']
                update[self.columns[item.column()]] = item.text()
                rewritedata = update.copy()
                self.db.re_record(id, update)
            except None as error:
                self.message(str(error))
                self.show_data(self.db.get_table_records())
                return
            self.changed = True
            self.db_data[item.row()] = rewritedata