# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M:\Programming\Python\projects\LabRabota_6_demo\widgets\mainWindow.ui'
#
# Created: Mon Oct 31 09:19:18 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 171)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_3 = QtGui.QLabel(self.splitter)
        self.label_3.setLineWidth(1)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.le_fio = QtGui.QLineEdit(self.splitter)
        self.le_fio.setAlignment(QtCore.Qt.AlignCenter)
        self.le_fio.setObjectName("le_fio")
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_4 = QtGui.QLabel(self.splitter_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.le_variant = QtGui.QLineEdit(self.splitter_2)
        self.le_variant.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.le_variant.setAlignment(QtCore.Qt.AlignCenter)
        self.le_variant.setObjectName("le_variant")
        self.verticalLayout.addWidget(self.splitter_3)
        self.pb_bezAS = QtGui.QPushButton(self.centralwidget)
        self.pb_bezAS.setObjectName("pb_bezAS")
        self.verticalLayout.addWidget(self.pb_bezAS)
        self.pb_sAS = QtGui.QPushButton(self.centralwidget)
        self.pb_sAS.setObjectName("pb_sAS")
        self.verticalLayout.addWidget(self.pb_sAS)
        self.pb_otchet = QtGui.QPushButton(self.centralwidget)
        self.pb_otchet.setObjectName("pb_otchet")
        self.verticalLayout.addWidget(self.pb_otchet)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Лабораторная работа № 6", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Лабораторная работа №6", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Анализ времени отработки вызова о происшествии", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Выполнил", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Вариант №", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_bezAS.setText(QtGui.QApplication.translate("MainWindow", "Часть 1. Прием и обработка вызова без применения АС", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_sAS.setText(QtGui.QApplication.translate("MainWindow", "Часть 2. Прием и обработка вызова с использованием АС", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_otchet.setText(QtGui.QApplication.translate("MainWindow", "Отчет", None, QtGui.QApplication.UnicodeUTF8))

