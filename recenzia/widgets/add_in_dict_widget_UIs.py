# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\operator.TEACHER\Dropbox\Programming\Python\projects\recenzia\widgets\add_in_dict_widget.ui'
#
# Created: Fri May 12 13:22:08 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 307)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.rb_part0 = QtGui.QRadioButton(Form)
        self.rb_part0.setObjectName("rb_part0")
        self.verticalLayout_3.addWidget(self.rb_part0)
        self.rb_part1 = QtGui.QRadioButton(Form)
        self.rb_part1.setObjectName("rb_part1")
        self.verticalLayout_3.addWidget(self.rb_part1)
        self.rb_part2 = QtGui.QRadioButton(Form)
        self.rb_part2.setObjectName("rb_part2")
        self.verticalLayout_3.addWidget(self.rb_part2)
        self.rb_part3 = QtGui.QRadioButton(Form)
        self.rb_part3.setObjectName("rb_part3")
        self.verticalLayout_3.addWidget(self.rb_part3)
        self.rb_part4 = QtGui.QRadioButton(Form)
        self.rb_part4.setObjectName("rb_part4")
        self.verticalLayout_3.addWidget(self.rb_part4)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.rb_group = QtGui.QRadioButton(Form)
        self.rb_group.setObjectName("rb_group")
        self.verticalLayout_3.addWidget(self.rb_group)
        self.rb_kat = QtGui.QRadioButton(Form)
        self.rb_kat.setObjectName("rb_kat")
        self.verticalLayout_3.addWidget(self.rb_kat)
        self.pb_result = QtGui.QRadioButton(Form)
        self.pb_result.setObjectName("pb_result")
        self.verticalLayout_3.addWidget(self.pb_result)
        self.rb_conformity = QtGui.QRadioButton(Form)
        self.rb_conformity.setObjectName("rb_conformity")
        self.verticalLayout_3.addWidget(self.rb_conformity)
        self.rb_lecturer = QtGui.QRadioButton(Form)
        self.rb_lecturer.setObjectName("rb_lecturer")
        self.verticalLayout_3.addWidget(self.rb_lecturer)
        self.rb_rank = QtGui.QRadioButton(Form)
        self.rb_rank.setObjectName("rb_rank")
        self.verticalLayout_3.addWidget(self.rb_rank)
        self.rb_position = QtGui.QRadioButton(Form)
        self.rb_position.setObjectName("rb_position")
        self.verticalLayout_3.addWidget(self.rb_position)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_add = QtGui.QPushButton(Form)
        self.pb_add.setObjectName("pb_add")
        self.verticalLayout.addWidget(self.pb_add)
        self.pb_edit = QtGui.QPushButton(Form)
        self.pb_edit.setObjectName("pb_edit")
        self.verticalLayout.addWidget(self.pb_edit)
        self.pb_del = QtGui.QPushButton(Form)
        self.pb_del.setObjectName("pb_del")
        self.verticalLayout.addWidget(self.pb_del)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "Оформление", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "Раздел 1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Form", "Раздел 2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Form", "Раздел 3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Form", "Схемы", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("Form", "Группы", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("Form", "Категория", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(7, QtGui.QApplication.translate("Form", "Результат", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(8, QtGui.QApplication.translate("Form", "Соответствие", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(9, QtGui.QApplication.translate("Form", "Преподаватель", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(10, QtGui.QApplication.translate("Form", "Звание", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(11, QtGui.QApplication.translate("Form", "Должность", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_part0.setText(QtGui.QApplication.translate("Form", "Оформление", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_part1.setText(QtGui.QApplication.translate("Form", "Раздел 1", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_part2.setText(QtGui.QApplication.translate("Form", "Раздел 2", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_part3.setText(QtGui.QApplication.translate("Form", "Раздел 3", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_part4.setText(QtGui.QApplication.translate("Form", "Схемы", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_group.setText(QtGui.QApplication.translate("Form", "Группы", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_kat.setText(QtGui.QApplication.translate("Form", "Категория", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_result.setText(QtGui.QApplication.translate("Form", "Результат", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_conformity.setText(QtGui.QApplication.translate("Form", "Соответствие", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_lecturer.setText(QtGui.QApplication.translate("Form", "Преподаватель", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_rank.setText(QtGui.QApplication.translate("Form", "Звание", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_position.setText(QtGui.QApplication.translate("Form", "Должность", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_add.setText(QtGui.QApplication.translate("Form", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_edit.setText(QtGui.QApplication.translate("Form", "Редактировать", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_del.setText(QtGui.QApplication.translate("Form", "Удалить", None, QtGui.QApplication.UnicodeUTF8))

