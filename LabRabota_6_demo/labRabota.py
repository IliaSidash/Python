import ctypes
from PySide.QtCore import *
from PySide.QtGui import *

import bezAS
import connect_database
import otchet
import root_dir
import sAS
from widgets import mainWindow_UIs as ui

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')


class labRabotaClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(labRabotaClass, self).__init__()
        self.setupUi(self)

        # UI
        self.setWindowIcon(QIcon(root_dir.png))

        # connects
        self.pb_bezAS.clicked.connect(self.openWidgetBezAS)
        self.pb_sAS.clicked.connect(self.openWidgetAS)
        self.pb_otchet.clicked.connect(self.openOtchet)
        # start
        self.pb_sAS.setEnabled(1)

    def openWidgetBezAS(self):
        if self.le_fio.text():
            if self.le_variant.text():
                if len(self.le_variant.text()) == 2:
                    self.le_fio.setEnabled(0)
                    self.le_variant.setEnabled(0)
                    name = self.le_fio.text()
                    variant = self.le_variant.text()
                    self.dial = bezAS.bezASClass(name, variant)
                    self.dial.show()
                else:
                    self.showMassage('Вариант должен соответствовать номеру по журналу и состоять из двух цифр. Например "01"')
            else:
                self.showMassage('Введите ваш вариант!')
        else:
            self.showMassage('Введите ваши ФИО!')

    def openWidgetAS(self):
        if self.le_fio.text():
            if self.le_variant.text():
                if len(self.le_variant.text()) == 2:
                    self.le_fio.setEnabled(0)
                    self.le_variant.setEnabled(0)
                    name = self.le_fio.text()
                    variant = self.le_variant.text()
                    self.dial = sAS.ASClass(connect_database.select(), name)
                    self.dial.show()
                else:
                    self.showMassage('Вариант должен соответствовать номеру по журналу и состоять из двух цифр. Например "01"')
            else:
                self.showMassage('Введите ваш вариант!')
        else:
            self.showMassage('Введите ваши ФИО!')

    def openOtchet(self):
        try:
            name = self.le_fio.text()
            self.dial = otchet.otchetClass(name)
            self.dial.show()
        except FileNotFoundError:
            self.showMassage('Работа еще не выполнена!')

    def showMassage(self, msq):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(QIcon(root_dir.png))
        msgBox.setWindowTitle('Ошибка!')
        msq = msq
        msgBox.setText(msq)
        msgBox.exec_()

if __name__ == '__main__':
    app = QApplication([])
    w = labRabotaClass()
    w.show()
    app.exec_()