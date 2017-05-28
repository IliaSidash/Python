# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M:\Python\projects\LabRabota_6\widgets\soundWidget.ui'
#
# Created: Mon Jul 25 16:18:10 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 41)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_start = QtGui.QPushButton(Form)
        self.pb_start.setObjectName("pb_start")
        self.horizontalLayout.addWidget(self.pb_start)
        self.pb_stop = QtGui.QPushButton(Form)
        self.pb_stop.setObjectName("pb_stop")
        self.horizontalLayout.addWidget(self.pb_stop)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_start.setText(QtGui.QApplication.translate("Form", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_stop.setText(QtGui.QApplication.translate("Form", "Stop", None, QtGui.QApplication.UnicodeUTF8))

