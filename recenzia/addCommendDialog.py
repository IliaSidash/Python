from PySide.QtCore import *
from PySide.QtGui import *
import connect

class AddCommendDialog(QDialog):
    def __init__(self, index_tab):
        super(AddCommendDialog, self).__init__()
        self.ly = QVBoxLayout(self)
        self.cb = QComboBox()
        self.ly.addWidget(self.cb)

        self.ok_btn = QPushButton('Добавить')
        self.ly.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton('Отмена')
        self.ly.addWidget(self.cancel_btn)

        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

        self.get_errors(index_tab)

    def get_errors(self, index_tab):
        table_sql = ('zero_part', 'first_part', 'second_part', 'third_part', 'fourth_part')
        sql = """SELECT error FROM """ + table_sql[index_tab]
        tuple = connect.get_errors(sql)
        for i in tuple:
            self.cb.addItem(i[0])

    def get_data(self):
        return self.cb.currentText()
