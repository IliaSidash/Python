import ctypes
import datetime
import os
from time import sleep

from PySide.QtCore import *
from PySide.QtGui import *
from pygame import mixer

import connect_database
import root_dir
from widgets import widgetsAS_UIs as ui

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')


BASE_DIR = root_dir.getRootDir()


class ASClass(QWidget, ui.Ui_Form):
    def __init__(self, dict, name):
        super(ASClass, self).__init__()
        self.setupUi(self)
        self.name = name
        self.dict = dict
        # connects
        self.pb_fire.clicked.connect(self.fire)
        self.pb_vyzov.clicked.connect(self.vyzov)
        self.le_FIO.editingFinished.connect(self.ppr)
        self.cb_postradavshie.toggled.connect(self.postradavshie)
        # start
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)

        arr = connect_database.select_street()

        completer = QCompleter(arr)
        self.le_ulica.setCompleter(completer)

        # UI
        self.le_postradavshie.setDisabled(1)
        self.cbEnabled()
        self.leDisabled(0)
        self.pb_vyzov.setEnabled(0)
        self.setWindowIcon(QIcon(root_dir.png))

        self.hh = 0
        self.mm = 0
        self.ss = 0
        self.n = 0
        self.ss_1 = 0

    def showMassage(self):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(QIcon('K:\Python\projects\LabRabota_6/01.png'))
        msgBox.setWindowTitle('Ошибка!')
        msq = 'Не верно выбраны подразделения!'
        msgBox.setText(msq)
        msgBox.exec_()

    def postradavshie(self):
        if self.cb_postradavshie.isChecked():
            self.le_postradavshie.setDisabled(0)
        else:
            self.le_postradavshie.setEnabled(0)

    def ppr(self):
        self.u = self.le_ulica.text().upper()
        self.d = self.le_dom.text()
        self.F = self.le_FIO.text()

        data = connect_database.ppr(self.u, self.d)
        rang = data[0]
        raion = data[1]
        podraionVyezda = data[2]


        if rang == 1:
            if raion == 1:
                self.cb_psch1.setChecked(1)
            elif raion == 6:
                self.cb_psch6.setChecked(1)
            elif raion == 11:
                self.cb_psch11.setChecked(1)
            elif raion == 16:
                self.cb_psch16.setChecked(1)
        elif rang == 2:
            if raion == 1:
                if podraionVyezda == 3:
                    self.cb_psch1.setChecked(1)
                    self.cb_psch2.setChecked(1)
                    self.cb_psch3.setChecked(1)
                    self.cb_psch4.setChecked(1)
                    self.cb_psch5.setChecked(1)
                elif podraionVyezda == 4:
                    self.cb_psch1.setChecked(1)
                    self.cb_psch12.setChecked(1)
                    self.cb_psch13.setChecked(1)
                    self.cb_psch4.setChecked(1)
                    self.cb_psch15.setChecked(1)
                elif podraionVyezda == 5:
                    self.cb_psch1.setChecked(1)
                    self.cb_psch5.setChecked(1)
                    self.cb_psch6.setChecked(1)
                    self.cb_psch7.setChecked(1)
                    self.cb_psch8.setChecked(1)
            elif raion == 6:
                if podraionVyezda == 8:
                    self.cb_psch6.setChecked(1)
                    self.cb_psch10.setChecked(1)
                    self.cb_psch9.setChecked(1)
                    self.cb_psch7.setChecked(1)
                    self.cb_psch8.setChecked(1)
                elif podraionVyezda == 9:
                    self.cb_psch6.setChecked(1)
                    self.cb_psch7.setChecked(1)
                    self.cb_psch11.setChecked(1)
                    self.cb_psch9.setChecked(1)
                    self.cb_psch12.setChecked(1)
                elif podraionVyezda == 10:
                    self.cb_psch6.setChecked(1)
                    self.cb_psch2.setChecked(1)
                    self.cb_psch16.setChecked(1)
                    self.cb_psch7.setChecked(1)
                    self.cb_psch10.setChecked(1)
            elif raion == 11:
                if podraionVyezda == 13:
                    self.cb_psch11.setChecked(1)
                    self.cb_psch15.setChecked(1)
                    self.cb_psch14.setChecked(1)
                    self.cb_psch12.setChecked(1)
                    self.cb_psch13.setChecked(1)
                elif podraionVyezda == 14:
                    self.cb_psch11.setChecked(1)
                    self.cb_psch6.setChecked(1)
                    self.cb_psch5.setChecked(1)
                    self.cb_psch8.setChecked(1)
                    self.cb_psch14.setChecked(1)
                elif podraionVyezda == 15:
                    self.cb_psch11.setChecked(1)
                    self.cb_psch4.setChecked(1)
                    self.cb_psch7.setChecked(1)
                    self.cb_psch6.setChecked(1)
                    self.cb_psch15.setChecked(1)
            elif raion == 16:
                if podraionVyezda == 18:
                    self.cb_psch16.setChecked(1)
                    self.cb_psch19.setChecked(1)
                    self.cb_psch20.setChecked(1)
                    self.cb_psch17.setChecked(1)
                    self.cb_psch18.setChecked(1)
                elif podraionVyezda == 19:
                    self.cb_psch16.setChecked(1)
                    self.cb_psch5.setChecked(1)
                    self.cb_psch9.setChecked(1)
                    self.cb_psch19.setChecked(1)
                    self.cb_psch10.setChecked(1)
                elif podraionVyezda == 20:
                    self.cb_psch16.setChecked(1)
                    self.cb_psch18.setChecked(1)
                    self.cb_psch11.setChecked(1)
                    self.cb_psch10.setChecked(1)
                    self.cb_psch20.setChecked(1)

    def cbEnabled(self):
        self.cb_psch1.setEnabled(0)
        self.cb_psch1.setChecked(0)
        self.cb_psch2.setEnabled(0)
        self.cb_psch2.setChecked(0)
        self.cb_psch3.setEnabled(0)
        self.cb_psch3.setChecked(0)
        self.cb_psch4.setEnabled(0)
        self.cb_psch4.setChecked(0)
        self.cb_psch5.setEnabled(0)
        self.cb_psch5.setChecked(0)
        self.cb_psch6.setEnabled(0)
        self.cb_psch6.setChecked(0)
        self.cb_psch7.setEnabled(0)
        self.cb_psch7.setChecked(0)
        self.cb_psch8.setEnabled(0)
        self.cb_psch8.setChecked(0)
        self.cb_psch9.setEnabled(0)
        self.cb_psch9.setChecked(0)
        self.cb_psch10.setEnabled(0)
        self.cb_psch10.setChecked(0)
        self.cb_psch11.setEnabled(0)
        self.cb_psch11.setChecked(0)
        self.cb_psch12.setEnabled(0)
        self.cb_psch12.setChecked(0)
        self.cb_psch13.setEnabled(0)
        self.cb_psch13.setChecked(0)
        self.cb_psch14.setEnabled(0)
        self.cb_psch14.setChecked(0)
        self.cb_psch15.setEnabled(0)
        self.cb_psch15.setChecked(0)
        self.cb_psch16.setEnabled(0)
        self.cb_psch16.setChecked(0)
        self.cb_psch17.setEnabled(0)
        self.cb_psch17.setChecked(0)
        self.cb_psch18.setEnabled(0)
        self.cb_psch18.setChecked(0)
        self.cb_psch19.setEnabled(0)
        self.cb_psch19.setChecked(0)
        self.cb_psch20.setEnabled(0)
        self.cb_psch20.setChecked(0)

    def cbDisabled(self):
        self.cb_psch1.setEnabled(1)
        self.cb_psch2.setEnabled(1)
        self.cb_psch3.setEnabled(1)
        self.cb_psch4.setEnabled(1)
        self.cb_psch5.setEnabled(1)
        self.cb_psch6.setEnabled(1)
        self.cb_psch7.setEnabled(1)
        self.cb_psch8.setEnabled(1)
        self.cb_psch9.setEnabled(1)
        self.cb_psch10.setEnabled(1)
        self.cb_psch11.setEnabled(1)
        self.cb_psch12.setEnabled(1)
        self.cb_psch13.setEnabled(1)
        self.cb_psch14.setEnabled(1)
        self.cb_psch15.setEnabled(1)
        self.cb_psch16.setEnabled(1)
        self.cb_psch17.setEnabled(1)
        self.cb_psch18.setEnabled(1)
        self.cb_psch19.setEnabled(1)
        self.cb_psch20.setEnabled(1)

    def clearTextFromLineEdit(self):
        self.le_ulica.clear()
        self.le_dom.clear()
        self.le_FIO.clear()
        self.le_postradavshie.clear()
        self.le_chto.clear()
        self.cb_postradavshie.setChecked(0)

    def vyzov(self):
        if self.cb_psch1.isChecked() or self.cb_psch2.isChecked() or self.cb_psch3.isChecked() or self.cb_psch4.isChecked() or self.cb_psch5.isChecked() or self.cb_psch6.isChecked()\
                or self.cb_psch7.isChecked() or self.cb_psch8.isChecked() or self.cb_psch9.isChecked() or self.cb_psch10.isChecked() or self.cb_psch11.isChecked()\
                or self.cb_psch12.isChecked() or self.cb_psch13.isChecked() or self.cb_psch14.isChecked() or self.cb_psch15.isChecked() or self.cb_psch16.isChecked():
            self.leDisabled(0)
            sleep(5 / 7)
            self.pb_vyzov.setEnabled(0)
            self.clearTextFromLineEdit()
            self.cbEnabled()
            self.lb_tekStatus.setText('Диспетчер 01 передает унифицированную карточку в выбранные ПСЧ!')
            self.enableButtom('Vyzov')
            self.lb_tekDatTime.clear()
            self.lb_soob.clear()
        else:
            self.showMassage()

    def startSound(self, n=1):
        if n == 1:
            path = os.path.join(BASE_DIR, 'sounds', (self.dict[self.n][0] + '.ogg')).encode(encoding='utf-8')
            self.n += 1
        elif n == 2:
            path = os.path.join(BASE_DIR, 'sounds', (self.dict[self.n][1] + '.ogg')).encode(encoding='utf-8')
        mixer.init()
        sound = mixer.Sound(path)
        self.t = sound.get_length()
        return sound.play()

    def fire(self):
        self.setStatus('Очевидец сообщает информацию о пожаре диспетчеру 01')
        self.startSound()
        self.startTimer()
        self.lb_tekDatTime.setText(datetime.datetime.strftime(datetime.datetime.now(), "%d.%m.%Y %H:%M:%S"))
        self.leDisabled(1)
        self.pb_fire.setEnabled(0)
        self.thread_sleep()

    def thread_sleep(self, n=1):
        self.obj = Thread_fire_sleep(self.t, n)
        self.thread = QThread()
        self.obj.moveToThread(self.thread)
        self.thread.started.connect(self.obj.tread_sleep)
        self.obj.finishSignal.connect(self.thread.quit)
        self.obj.finishSignal.connect(self.enableButtom)
        self.thread.start()

    def setStatus(self, status):
        self.lb_tekStatus.setText(status)



    def leDisabled(self, a):
        self.le_dom.setEnabled(a)
        self.le_FIO.setEnabled(a)
        self.le_ulica.setEnabled(a)
        self.le_chto.setEnabled(a)
        self.label.setEnabled(a)
        self.label_2.setEnabled(a)
        self.label_3.setEnabled(a)
        self.label_6.setEnabled(a)
        self.label_5.setEnabled(a)
        self.cb_postradavshie.setEnabled(a)

    def enableButtom(self, v):
        if self.n <= 5:
            if v == 'Fire':
                self.pb_vyzov.setEnabled(1)
                self.cbDisabled()
            elif v == 'Vyzov':
                self.stopTimer()
                self.pb_fire.setEnabled(1)
                self.cbEnabled()
                if self.n == 5:
                    ASClass.close(self)

    def setInfo(self, i):
        self.lb_soob.setText(i)

    def startTimer(self):
        self.timer.start(1000)

    def stopTimer(self):
        self.timer.stop()
        self.saveRezult()

    def showTime(self):
        self.ss += 1
        self.ss_1 += 1
        if self.ss % 60 == 0:
            self.ss = 0
            self.mm += 1
            if self.mm % 60 == 0:
                self.mm = 0
                self.hh += 1
        self.time = datetime.time(self.hh, self.mm, self.ss)
        self.lb_time.setText(str(self.time))

    def saveRezult(self):
        name = self.name + '.txt'
        with open(name, 'a', encoding='utf-8') as f:
            f.write('Вызов №' + str(self.n) + '. Время отработки вызова с использованием АС: ' + str(self.time)+ ' = ' + str(self.ss_1)+ ' секунд\n')
            self.ss_1 = 0

class Thread_fire_sleep(QObject):
    finishSignal = Signal(str)
    def __init__(self, t, n):
        super(Thread_fire_sleep, self).__init__()
        self.t = t
        self.n = n

    def tread_sleep(self):
        sleep(self.t)
        if self.n == 1:
            self.finishSignal.emit('Fire')
        elif self.n == 2:
            self.finishSignal.emit('Vyzov')

