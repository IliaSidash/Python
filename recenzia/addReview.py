from PySide.QtCore import *
from PySide.QtGui import *
from widgets import add_review_widget_UIs as ui
import connect,  mainWindow, template, addInDict
import AddCommendDialog as dial

class AddReview(QWidget, ui.Ui_Form):
    def __init__(self, name=None):
        super(AddReview, self).__init__()
        self.setupUi(self)
        self.name = name
        self.dateEdit.setDate(QDate.currentDate())
        self.start()

        #connect
        self.pb_ok.clicked.connect(self.close_window_with_save)
        self.pb_add.clicked.connect(self.add_commend)
        self.pb_del.clicked.connect(self.del_commend)
        self.pb_cancel.clicked.connect(self.close_window_without_save)
        self.pb_print.clicked.connect(self.get_data_for_report)
        self.pb_dict.clicked.connect(self.open_widget_addInDict)

    def open_widget_addInDict(self):
        self.dial = addInDict.AddInDict()
        return self.dial.show()


    def start(self):
        self.get_kategory()
        self.get_groups()
        self.get_name()
        self.get_position()
        self.get_rank()
        self.get_rezult()
        self.get_conformity()
        self.fill_table_commend()
        if self.name != None:
            self.edit()



# Заполнение комбобоксов данными -----------------------------------

    def get_kategory(self):
        tuple = connect.get_kategory()
        for i in tuple:
            self.cb_kat.addItem(i[1])

    def get_groups(self):
        tuple = connect.get_group()
        for i in tuple:
            self.cb_group.addItem(i[1])

    def get_conformity(self):
        tuple = connect.get_conformity()
        for i in tuple:
            self.cb_conformity.addItem(i[0])

    def get_position(self):
        tuple = connect.get_position()
        for i in tuple:
            self.cb_position.addItem(i[0])

    def get_name(self):
        tuple = connect.get_name()
        for i in tuple:
            self.cb_name.addItem(i[0])

    def get_rank(self):
        tuple = connect.get_rank()
        for i in tuple:
            self.cb_rank.addItem(i[0])

    def get_rezult(self):
        tuple = connect.get_rezult()
        for i in tuple:
            self.cb_rezult.addItem(i[0])

# Добавление замечаний -------------------------
    def add_commend(self):
        index_tab = self.tabwidget.currentIndex()
        if index_tab == 0:
            sql = """SELECT zero_part.id_error, Name.id_name FROM zero_part, Name WHERE zero_part.error=(?) AND Name.name=(?)"""
            sql2 = """INSERT INTO commend_zeropart (id_error, id_name) VALUES(?,?)"""
        elif index_tab == 1:
            sql = """SELECT first_part.id_error, Name.id_name FROM first_part, Name WHERE first_part.error=(?) AND Name.name=(?)"""
            sql2 = """INSERT INTO commend_firstpart (id_error, id_name) VALUES(?,?)"""
        elif index_tab == 2:
            sql = """SELECT second_part.id_error, Name.id_name FROM second_part, Name WHERE second_part.error=(?) AND Name.name=(?)"""
            sql2 = """INSERT INTO commend_secondpart (id_error, id_name) VALUES(?,?)"""
        elif index_tab == 3:
            sql = """SELECT third_part.id_error, Name.id_name FROM third_part, Name WHERE third_part.error=(?) AND Name.name=(?)"""
            sql2 = """INSERT INTO commend_thirdpart (id_error, id_name) VALUES(?,?)"""
        elif index_tab == 4:
            sql = """SELECT fourth_part.id_error, Name.id_name FROM fourth_part, Name WHERE fourth_part.error=(?) AND Name.name=(?)"""
            sql2 = """INSERT INTO commend_fourthpart (id_error, id_name) VALUES(?,?)"""
        self.add_name()
        name = self.le_name.text()
        self.dial = dial.AddCommendDialog(index_tab)
        r = self.dial.exec_()
        if r:
            commend = self.dial.get_data()
            connect.add_commend(sql, sql2, commend, name)
            self.fill_table_commend()

# Удаление замечаний -----------------------------
    def del_commend(self):
        tab_widget = (self.tw_part0, self.tw_part1, self.tw_part2, self.tw_part3, self.tw_part4)
        index = self.tabwidget.currentIndex()
        if tab_widget[index].currentItem() and tab_widget[index].currentItem().isSelected():
            commend = tab_widget[index].currentItem().text()
            connect.del_commend(commend, index)
            self.fill_table_commend()


# Добавление обучающегося -------------------------

    def get_data_for_add_name(self):
        number = self.le_number.text()
        name = self.le_name.text()
        kat = connect.get_id_kategory(self.cb_kat.currentText())
        group = connect.get_id_group(self.cb_group.currentText())
        conformity = connect.get_id_conformity(self.cb_conformity.currentText())
        lecturer = connect.get_id_lecturer(self.cb_name.currentText())
        position = connect.get_id_position(self.cb_position.currentText())
        rank = connect.get_id_rank(self.cb_rank.currentText())
        date = self.dateEdit.text()
        rezult = connect.get_id_rezult(self.cb_rezult.currentText())
        return (number, name, kat, group, conformity, lecturer, position, rank, date, rezult)

    def add_name(self):
        connect.add_name(self.get_data_for_add_name())

# Закрытие окна добавления обучающегося ---------------------

    def close_window_with_save(self):
        self.add_name()
        AddReview.close(self)

    def close_window_without_save(self):
        AddReview.close(self)

# Заполенение таблицы с замечаниями -------------------------

    def fill_table_commend(self):
        name = self.le_name.text()
        self.data = dict()
        if len(name) > 0:
            table_sql2 = ('commend_zeropart', 'commend_firstpart', 'commend_secondpart', 'commend_thirdpart', 'commend_fourthpart')
            table_sql3 = ('zero_part', 'first_part', 'second_part', 'third_part', 'fourth_part')
            for i in range(self.tabwidget.count()):
                sql2 = """SELECT id_error FROM """ + table_sql2[i] + """ WHERE id_name=(?)"""
                sql3 = """SELECT """+ table_sql3[i] + """.error FROM """ + table_sql3[i] + """ WHERE """ + table_sql3[i] + """.id_error=(?)"""
                data = connect.view_error(name, sql2, sql3)
                self.data[i] = data
                tab_widget = (self.tw_part0, self.tw_part1, self.tw_part2, self.tw_part3, self.tw_part4)
                tab_widget[i].setColumnCount(1)
                tab_widget[i].setRowCount(len(data))
                tab_widget[i].verticalHeader().hide()
                tab_widget[i].setHorizontalHeaderLabels(['Замечание'])
                tab_widget[i].horizontalHeader().setResizeMode(QHeaderView.Stretch)
                for item, d in enumerate(data):
                    self.item = QTableWidgetItem()
                    self.item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.item.setText(d)
                    tab_widget[i].setItem(0, item, self.item)


# Редактирование обучающегося --------------------------------------

    def edit(self):
        data = connect.select_for_edit(self.name)
        self.le_number.setText(str(data[0]))
        self.le_name.setText(self.name)
        self.cb_kat.setCurrentIndex(self.cb_kat.findText(data[4]))
        self.cb_group.setCurrentIndex(self.cb_group.findText(data[3]))
        self.cb_conformity.setCurrentIndex(self.cb_conformity.findText(data[6]))
        self.cb_name.setCurrentIndex(self.cb_name.findText(data[5]))
        self.cb_position.setCurrentIndex(self.cb_position.findText(data[7]))
        self.cb_rank.setCurrentIndex(self.cb_rank.findText(data[8]))
        self.dateEdit.setDate(QDate.fromString(data[2], "dd.MM.yyyy"))
        self.cb_rezult.setCurrentIndex(self.cb_rezult.findText(data[1]))
        self.fill_table_commend()

# Печать отчета ----------------------------

    def get_data_for_report(self):
        self.add_name()
        name = self.le_name.text()
        data = connect.select_for_edit(name)
        data_key_errors = self.data
        template.create_report(name, data, data_key_errors)
