from PySide.QtCore import *
from PySide.QtGui import *
from widgets import main_window_widget_UIs as ui
import addReview, connect, addInDict

class MainWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.start()
        self.tableWidget.selectRow(self.tableWidget.currentRow())

    # connect
        self.pb_search.clicked.connect(self.search)
        self.pb_add.clicked.connect(self.open_widget_addReview)
        self.pb_edit.clicked.connect(self.edit)
        self.pb_del.clicked.connect(self.delete)
        self.tableWidget.cellClicked.connect(self.select_row)
        self.pb_sync.clicked.connect(self.fill_table)
        self.pb_dict.clicked.connect(self.open_widget_addToDict)

    def printer(self):
        print('Hello')

    def open_widget_addReview(self):
        self.dial = addReview.AddReview()
        self.dial.show()

    def open_widget_addToDict(self):
        self.dial = addInDict.AddInDict()
        return self.dial.show()

    def start(self):
        self.get_kategory()
        self.get_groups()
        self.get_rezult()
        self.get_lecturer_name()
        self.fill_table()

    def fill_table(self):
        data = connect.view_db()
        count = 0
        row = 0
        for i in data:
            count += 1
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(count)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        for i, d in enumerate(data):
            for ii in d:
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item.setText(str(ii))
                self.tableWidget.setItem(i, row, item)
                if row < 6:
                    row += 1
                else:
                    row = 0

    def get_groups(self):
        tuple = connect.get_group()
        for i in tuple:
            self.cb_group.addItem(i[1])

    def get_kategory(self):
        tuple = connect.get_kategory()
        for i in tuple:
            self.cb_kategory.addItem(i[1])

    def get_rezult(self):
        tuple = connect.get_rezult()
        for i in tuple:
            self.cb_rezult.addItem(i[0])

    def get_lecturer_name(self):
        tuple = connect.get_lecturer_name()
        for i in tuple:
            self.cb_lecturer.addItem(i[0])

    def search(self):
        pass

    def select_row(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow())

    def edit(self):
        try:
            name = self.tableWidget.selectedItems()[1].text()
        except IndexError:
            self.dial = QMessageBox()
            self.dial.setText("Не выбран параметр редактирования")
            self.dial.exec_()
        else:
            self.dial = addReview.AddReview(name)
            self.dial.show()

    def delete(self):
        name = self.tableWidget.selectedItems()[1].text()
        connect.del_name(name)
        self.fill_table()

if __name__ == '__main__':
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec_()