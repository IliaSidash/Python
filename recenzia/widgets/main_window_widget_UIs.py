# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\operator.TEACHER\Dropbox\Programming\Python\projects\recenzia\widgets\main_window_widget.ui'
#
# Created: Thu May  4 14:25:18 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(426, 505)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.le_name = QtGui.QLineEdit(self.centralwidget)
        self.le_name.setObjectName("le_name")
        self.gridLayout.addWidget(self.le_name, 1, 1, 1, 2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 7, 0, 1, 5)
        self.cb_kategory = QtGui.QComboBox(self.centralwidget)
        self.cb_kategory.setObjectName("cb_kategory")
        self.gridLayout.addWidget(self.cb_kategory, 2, 1, 1, 2)
        self.cb_group = QtGui.QComboBox(self.centralwidget)
        self.cb_group.setObjectName("cb_group")
        self.gridLayout.addWidget(self.cb_group, 3, 1, 1, 2)
        self.cb_rezult = QtGui.QComboBox(self.centralwidget)
        self.cb_rezult.setObjectName("cb_rezult")
        self.gridLayout.addWidget(self.cb_rezult, 4, 1, 1, 2)
        self.cb_lecturer = QtGui.QComboBox(self.centralwidget)
        self.cb_lecturer.setObjectName("cb_lecturer")
        self.gridLayout.addWidget(self.cb_lecturer, 5, 1, 1, 2)
        self.le_number = QtGui.QLineEdit(self.centralwidget)
        self.le_number.setObjectName("le_number")
        self.gridLayout.addWidget(self.le_number, 0, 1, 1, 2)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)
        self.pb_add = QtGui.QPushButton(self.centralwidget)
        self.pb_add.setObjectName("pb_add")
        self.gridLayout.addWidget(self.pb_add, 0, 4, 1, 1)
        self.pb_edit = QtGui.QPushButton(self.centralwidget)
        self.pb_edit.setObjectName("pb_edit")
        self.gridLayout.addWidget(self.pb_edit, 1, 4, 1, 1)
        self.pb_del = QtGui.QPushButton(self.centralwidget)
        self.pb_del.setObjectName("pb_del")
        self.gridLayout.addWidget(self.pb_del, 2, 4, 1, 1)
        self.pb_search = QtGui.QPushButton(self.centralwidget)
        self.pb_search.setObjectName("pb_search")
        self.gridLayout.addWidget(self.pb_search, 6, 0, 1, 3)
        self.pb_report = QtGui.QPushButton(self.centralwidget)
        self.pb_report.setObjectName("pb_report")
        self.gridLayout.addWidget(self.pb_report, 4, 4, 1, 1)
        self.pb_dict = QtGui.QPushButton(self.centralwidget)
        self.pb_dict.setObjectName("pb_dict")
        self.gridLayout.addWidget(self.pb_dict, 5, 4, 1, 1)
        self.pb_sync = QtGui.QPushButton(self.centralwidget)
        self.pb_sync.setObjectName("pb_sync")
        self.gridLayout.addWidget(self.pb_sync, 6, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.le_number, self.le_name)
        MainWindow.setTabOrder(self.le_name, self.cb_kategory)
        MainWindow.setTabOrder(self.cb_kategory, self.cb_group)
        MainWindow.setTabOrder(self.cb_group, self.cb_rezult)
        MainWindow.setTabOrder(self.cb_rezult, self.cb_lecturer)
        MainWindow.setTabOrder(self.cb_lecturer, self.pb_search)
        MainWindow.setTabOrder(self.pb_search, self.pb_add)
        MainWindow.setTabOrder(self.pb_add, self.pb_edit)
        MainWindow.setTabOrder(self.pb_edit, self.pb_del)
        MainWindow.setTabOrder(self.pb_del, self.tableWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Рецензия", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Преподаватель", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Результат", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Фамилия И.О.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Категория", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Группа", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "№п/п", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Фамилия И.О.", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Результат проверки", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Дата", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Группа", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Категория", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "Преподаватель", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "№п/п", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_add.setText(QtGui.QApplication.translate("MainWindow", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_edit.setText(QtGui.QApplication.translate("MainWindow", "Редактировать", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_del.setText(QtGui.QApplication.translate("MainWindow", "Удалить", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_search.setText(QtGui.QApplication.translate("MainWindow", "Поиск", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_report.setText(QtGui.QApplication.translate("MainWindow", "Отчет", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_dict.setText(QtGui.QApplication.translate("MainWindow", "Словари", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_sync.setText(QtGui.QApplication.translate("MainWindow", "Синхронизация", None, QtGui.QApplication.UnicodeUTF8))
