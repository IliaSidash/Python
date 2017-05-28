from PySide.QtCore import *
from PySide.QtGui import *
from widgets import add_in_dict_widget_UIs as ui
import connect, addInDictDialog

class AddInDict(QWidget, ui.Ui_Form):
    def __init__(self):
        super(AddInDict, self).__init__()
        self.setupUi(self)
        self.tuple_table = ('zero_part', 'first_part', 'second_part',
                            'third_part', 'fourth_part', 'Groups',
                            'kategory', 'Rezult', 'Conformity',
                            'Lecturer_name', 'Rank', 'Position')

        self.tuple_param = ('error', 'error', 'error',
                            'error', 'error', 'group_groups',
                            'kategory', 'rezult', 'conformity',
                            'lecturer_name', 'rank', 'position')

        self.tuple_id_param = ('id_error', 'id_error', 'id_error',
                            'id_error', 'id_error', 'id_group',
                            'id_kategory', 'id_rezult', 'id_conformity',
                            'id_lecturer_name', 'id_rank', 'id_position')

        # connects
        self.comboBox.currentIndexChanged.connect(self.view_dicts)
        self.pb_add.clicked.connect(self.add_param_in_dict)
        self.pb_edit.clicked.connect(self.edit_param_in_dict)

        # start
        self.view_dicts()



    def view_dicts(self):

        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(len(connect.view_dicts(self.tuple_table[self.comboBox.currentIndex()])))
        self.tableWidget.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().hide()
        for i, text in enumerate(connect.view_dicts(self.tuple_table[self.comboBox.currentIndex()])):
            self.item = QTableWidgetItem()
            self.item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.item.setText(text[1])
            self.tableWidget.setItem(0, i, self.item)

    def add_param_in_dict(self):
        table = self.tuple_table[self.comboBox.currentIndex()]

        par = self.tuple_param[self.comboBox.currentIndex()]
        self.dial = addInDictDialog.AddInDictDialog()
        r = self.dial.exec_()
        if r and len(self.dial.lineEdit.text()) > 0:
            text = self.dial.lineEdit.text()
            connect.add_param_in_dict(table, par, text)
        self.view_dicts()

    def edit_param_in_dict(self):
        try:
            text = self.tableWidget.currentItem().text()
        except AttributeError:
            self.dial = QMessageBox()
            self.dial.setText("Не выбран параметр редактирования")
            self.dial.exec_()
        else:
            par = self.tuple_param[self.comboBox.currentIndex()]
            table = self.tuple_table[self.comboBox.currentIndex()]
            id_par = self.tuple_id_param[self.comboBox.currentIndex()]
            self.dial = addInDictDialog.AddInDictDialog()
            self.dial.lineEdit.setText(text)
            r = self.dial.exec_()
            if r and len(self.dial.lineEdit.text()) > 0:
                new_text = self.dial.lineEdit.text()
                connect.edit_param_in_dict(id_par, par, table, text, new_text)
                self.view_dicts()
