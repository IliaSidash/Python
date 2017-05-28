# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'K:\Python\projects\LabRabota_6\widgets\widgetOtchet.ui'
#
# Created: Tue May 17 13:20:51 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 78)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_3 = QtGui.QSplitter(Form)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lb_otchet = QtGui.QLabel(self.splitter)
        self.lb_otchet.setText("")
        self.lb_otchet.setObjectName("lb_otchet")
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.verticalLayout.addWidget(self.splitter_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Отчет", None, QtGui.QApplication.UnicodeUTF8))

