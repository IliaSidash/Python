import ctypes
import datetime
import os
from time import sleep

from PySide.QtCore import *
from PySide.QtGui import *
from pygame import mixer

import connect_database
import root_dir
import sAS
from widgets import widgetBezAS_UIs as ui

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

BASE_DIR = root_dir.getRootDir()


class bezASClass(QWidget, ui.Ui_Form):
    def __init__(self, name, variant):
        super(bezASClass, self).__init__()
        self.setupUi(self)

        # UI
        self.setWindowIcon(QIcon(root_dir.png))

        # connects
        self.pb_fire.clicked.connect(self.fire)
        self.pb_vyzov.clicked.connect(self.vyzov)

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.cbEnabled()
        self.pb_vyzov.setEnabled(0)

        self.hh = 0
        self.mm = 0
        self.ss = 0
        self.ss_1 = 0
        self.n = 0
        self.name = name
        self.variant = variant

    def ppr(self):
            dict = connect_database.select()
            nomerVyzova = dict[self.n][2]
            raionVyezda = dict[self.n][3]
            podraionVyezda = dict[self.n][4]
            if nomerVyzova == 1:
                if raionVyezda == 1:
                    if self.cb_psch1.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 6:
                    if self.cb_psch6.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 11:
                    if self.cb_psch11.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 16:
                    if self.cb_psch16.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()

            elif nomerVyzova == 2:
                if raionVyezda == 1 and podraionVyezda == 3:
                    if self.cb_psch1.isChecked() and self.cb_psch2.isChecked() and self.cb_psch3.isChecked() and self.cb_psch4.isChecked() and self.cb_psch5.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 1 and podraionVyezda == 4:
                    if self.cb_psch1.isChecked() and self.cb_psch12.isChecked() and self.cb_psch13.isChecked() and self.cb_psch15.isChecked() and self.cb_psch4.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 1 and podraionVyezda == 5:
                    if self.cb_psch1.isChecked() and self.cb_psch5.isChecked() and self.cb_psch6.isChecked() and self.cb_psch7.isChecked() and self.cb_psch8.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 6 and podraionVyezda == 8:
                    if self.cb_psch6.isChecked() and self.cb_psch7.isChecked() and self.cb_psch8.isChecked() and self.cb_psch9.isChecked() and self.cb_psch10.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 6 and podraionVyezda == 9:
                    if self.cb_psch6.isChecked() and self.cb_psch7.isChecked() and self.cb_psch11.isChecked() and self.cb_psch9.isChecked() and self.cb_psch12.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 6 and podraionVyezda == 10:
                    if self.cb_psch6.isChecked() and self.cb_psch2.isChecked() and self.cb_psch16.isChecked() and self.cb_psch7.isChecked() and self.cb_psch10.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 11 and podraionVyezda == 13:
                    if self.cb_psch11.isChecked() and self.cb_psch12.isChecked() and self.cb_psch13.isChecked() and self.cb_psch14.isChecked() and self.cb_psch15.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 11 and podraionVyezda == 14:
                    if self.cb_psch11.isChecked() and self.cb_psch6.isChecked() and self.cb_psch5.isChecked() and self.cb_psch14.isChecked() and self.cb_psch8.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 11 and podraionVyezda == 15:
                    if self.cb_psch11.isChecked() and self.cb_psch6.isChecked() and self.cb_psch4.isChecked() and self.cb_psch15.isChecked() and self.cb_psch7.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 16 and podraionVyezda == 18:
                    if self.cb_psch16.isChecked() and self.cb_psch17.isChecked() and self.cb_psch18.isChecked() and self.cb_psch19.isChecked() and self.cb_psch20.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 16 and podraionVyezda == 19:
                    if self.cb_psch16.isChecked() and self.cb_psch9.isChecked() and self.cb_psch10.isChecked() and self.cb_psch5.isChecked() and self.cb_psch19.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()
                elif raionVyezda == 16 and podraionVyezda == 20:
                    if self.cb_psch16.isChecked() and self.cb_psch18.isChecked() and self.cb_psch10.isChecked() and self.cb_psch11.isChecked() and self.cb_psch20.isChecked():
                        self.vyzov()
                    else:
                        self.showMassage()

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

        self.pb_vyzov.setEnabled(1)


    def showMassage(self):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(QIcon('K:\Python\projects\LabRabota_6/01.png'))
        msgBox.setWindowTitle('Ошибка!')
        msq = 'Не верно выбраны подразделения!'
        msgBox.setText(msq)
        msgBox.exec_()

    def startSound(self, n=1):
        self.dict = connect_database.select()
        if n == 1:
            path = (os.path.join(BASE_DIR, 'sounds', (self.dict[self.n][0] + '.ogg'))).encode(encoding='utf-8')
        elif n == 2:
            path = (os.path.join(BASE_DIR, 'sounds', (self.dict[self.n][1] + '.ogg'))).encode(encoding='utf-8')
            self.n += 1
        mixer.init()
        sound = mixer.Sound(path)
        self.t = sound.get_length()
        return sound.play()

    def fire(self):
        self.setStatus('Очевидец сообщает информацию о пожаре диспетчеру 01')
        self.startTimer()
        self.startSound()
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

    def vyzov(self):
        self.setStatus('Диспетчер 01 оповещает необходимые ПСЧ')
        sleep(5 / 7)
        if self.n <= 4:
            self.pb_vyzov.setEnabled(0)
            # self.pb_fire.setEnabled(1)
            self.cbEnabled()
            self.startSound(2)
            self.thread_sleep(2)

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
                    bezASClass.close(self)
                    self.dial = sAS.ASClass(self.dict, self.name)
                    self.dial.show()

    def setStatus(self, status):
        self.lb_tekStatus.setText(status)

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
        self.setStatus('')
        name = self.name + '.txt'
        with open(name, 'a', encoding='utf-8') as f:
            f.write('Вызов №' + str(self.n) + '. Время отработки вызова без применения АС: ' + str(self.time)+ ' = ' + str(self.ss_1)+ ' секунд\n')
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


