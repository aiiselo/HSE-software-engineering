# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/olesyamartinyuk/PycharmProjects/Lab_3/design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 16))
        self.label.setObjectName("label")
        self.clear_publisher_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_publisher_button.setGeometry(QtCore.QRect(10, 450, 391, 32))
        self.clear_publisher_button.setObjectName("clear_publisher_button")
        self.clear_book_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_book_button.setGeometry(QtCore.QRect(410, 450, 391, 32))
        self.clear_book_button.setObjectName("clear_book_button")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(400, 30, 81, 32))
        self.search_button.setObjectName("search_button")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 30, 391, 33))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.data_to_delete = QtWidgets.QLineEdit(self.widget)
        self.data_to_delete.setObjectName("data_to_delete")
        self.horizontalLayout_7.addWidget(self.data_to_delete)
        self.delete_button = QtWidgets.QPushButton(self.widget)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_7.addWidget(self.delete_button)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 70, 391, 18))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 90, 391, 23))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.publisher_name = QtWidgets.QLineEdit(self.widget2)
        self.publisher_name.setObjectName("publisher_name")
        self.horizontalLayout_2.addWidget(self.publisher_name)
        self.publisher_telephone = QtWidgets.QLineEdit(self.widget2)
        self.publisher_telephone.setObjectName("publisher_telephone")
        self.horizontalLayout_2.addWidget(self.publisher_telephone)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(10, 140, 791, 301))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.publisher_table = QtWidgets.QTableWidget(self.widget3)
        self.publisher_table.setObjectName("publisher_table")
        self.publisher_table.setColumnCount(0)
        self.publisher_table.setRowCount(0)
        self.horizontalLayout.addWidget(self.publisher_table)
        self.book_table = QtWidgets.QTableWidget(self.widget3)
        self.book_table.setObjectName("book_table")
        self.book_table.setColumnCount(0)
        self.book_table.setRowCount(0)
        self.horizontalLayout.addWidget(self.book_table)
        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(410, 90, 391, 23))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.book_title = QtWidgets.QLineEdit(self.widget4)
        self.book_title.setObjectName("book_title")
        self.horizontalLayout_3.addWidget(self.book_title)
        self.book_author = QtWidgets.QLineEdit(self.widget4)
        self.book_author.setObjectName("book_author")
        self.horizontalLayout_3.addWidget(self.book_author)
        self.book_publisher = QtWidgets.QLineEdit(self.widget4)
        self.book_publisher.setObjectName("book_publisher")
        self.horizontalLayout_3.addWidget(self.book_publisher)
        self.widget5 = QtWidgets.QWidget(self.centralwidget)
        self.widget5.setGeometry(QtCore.QRect(410, 70, 391, 18))
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget5)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.widget6 = QtWidgets.QWidget(self.centralwidget)
        self.widget6.setGeometry(QtCore.QRect(10, 110, 791, 32))
        self.widget6.setObjectName("widget6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.add_to_publisher_button = QtWidgets.QPushButton(self.widget6)
        self.add_to_publisher_button.setObjectName("add_to_publisher_button")
        self.horizontalLayout_6.addWidget(self.add_to_publisher_button)
        self.add_to_book_button = QtWidgets.QPushButton(self.widget6)
        self.add_to_book_button.setObjectName("add_to_book_button")
        self.horizontalLayout_6.addWidget(self.add_to_book_button)
        self.widget7 = QtWidgets.QWidget(self.centralwidget)
        self.widget7.setGeometry(QtCore.QRect(550, 490, 251, 66))
        self.widget7.setObjectName("widget7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget7)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clear_all = QtWidgets.QPushButton(self.widget7)
        self.clear_all.setObjectName("clear_all")
        self.verticalLayout.addWidget(self.clear_all)
        self.delete_database_button = QtWidgets.QPushButton(self.widget7)
        self.delete_database_button.setObjectName("delete_database_button")
        self.verticalLayout.addWidget(self.delete_database_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionDelete)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter a book author"))
        self.clear_publisher_button.setText(_translate("MainWindow", "Clear all publisher records"))
        self.clear_book_button.setText(_translate("MainWindow", "Clear all book records"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.label_2.setText(_translate("MainWindow", "Publisher name"))
        self.label_3.setText(_translate("MainWindow", "Publisher tel. number"))
        self.label_4.setText(_translate("MainWindow", "Book title"))
        self.label_5.setText(_translate("MainWindow", "Book author"))
        self.label_6.setText(_translate("MainWindow", "Book publisher"))
        self.add_to_publisher_button.setText(_translate("MainWindow", "Add new record of publisher"))
        self.add_to_book_button.setText(_translate("MainWindow", "Add new record of book"))
        self.clear_all.setText(_translate("MainWindow", "Clear all records"))
        self.delete_database_button.setText(_translate("MainWindow", "Delete database"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Backspace"))
