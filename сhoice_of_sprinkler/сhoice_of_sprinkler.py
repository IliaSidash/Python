from PySide.QtCore import *
from PySide.QtGui import *
import main_menu_UIs as ui
import os, sys
from ctypes import *

kat = ((0.08, 0.9, 0.1, 0.11, 0.12, 0.13),
       (0.12, 0.13, 0.14, 0.16, 0.17, 0.18),
       (0.24, 0.26, 0.29, 0.31, 0.34, 0.36),
       (0.3, 0.33, 0.36, 0.39, 0.42, 0.45))

kat_5 = ((0.08, 0.088, 0.097, 0.106, 0.117, 0.129),
         (0.16, 0.176, 0.194, 0.213, 0.234, 0.258),
         (0.24, 0.264, 0.290, 0.319, 0.351, 0.387),
         (0.32, 0.352, 0.387, 0.426, 0.469, 0.515),
         (0.40, 0.440, 0.484, 0.532, 0.586, 0.644))

kat_6 = ((0.16, 0.176, 0.194, 0.213, 0.234, 0.258),
         (0.32, 0.352, 0.387, 0.426, 0.469, 0.515),
         (0.4, 0.440, 0.484, 0.532, 0.586, 0.644),
         (0.4, 0.440, 0.484, 0.532, 0.586, 0.644),
         (0.5, 0.550, 0.605, 0.666, 0.732, 0.805))

k_up = (0.24, 0.3, 0.35, 0.42, 0.47, 0.6, 0.77, 0.84, 1.28, 1.91)

markirovka_up = {0.24: 'CBO0-PBо(д)0,24-R1/2/P57(68, 79, 93, 141, 182).B3-«CBB-8»',
                 0.3: 'CBO0-PBо(д)0,30-R1/2/P57(68, 79, 93, 141, 182).B3-«CBB-К57»',
                 0.35: 'CBO0-PBо(д)0,35-R1/2/P57(68, 79, 93, 141, 182).B3-«CBB-10»',
                 0.42: 'CBO0-PBо(д)0,42-R1/2/P57(68, 79, 93, 141, 182).B3-«CBB-К80»',
                 0.47: 'CBO0-PBо(д)0,47-R1/2/P57(68, 79, 93, 141, 182).B3-«CBB-12»',
                 0.6: 'CBO0-PBо(д)0,60-R1/2/P57(68, 79, 93, 141, 182).B3-«CBB-К115»',
                 0.77: 'CBO0-PBо(д)0,77-R1/2/P57(68, 79, 93, 141, 182).B3-«CBB-15»',
                 0.84: 'CBO0-PBо(д)0,84-R1/2/P57(68, 79, 93, 141, 182).B3-«CBB-К160»',
                 1.28: 'СУS0-РВо 1,28-R3/4/Р68.В3–«СОБР-17-В» (СУS - В – 1,28 - 68. С)',
                 1.91: 'СУS0-РВо 1,91-R1/Р93.В3–«СОБР-25-В» (СУS - В – 1,91 - 93.С - R1)'}

markirovka_down = {0.24: 'CBO0-PНо(д)0,24-R1/2/P57(68, 79, 93, 141, 182).B3-«CBН-8»',
                   0.3: 'CBO0-PНо(д)0,30-R1/2/P57(68, 79, 93, 141, 182).B3-«CBН-К57»',
                   0.35: 'CBO0-PНо(д)0,35-R1/2/P57(68, 79, 93, 141, 182).B3-«CBН-10»',
                   0.42: 'CBO0-PНо(д)0,42-R1/2/P57(68, 79, 93, 141, 182).B3-«CBН-К80»',
                   0.47: 'CBO0-PНо(д)0,47-R1/2/P57(68, 79, 93, 141, 182).B3-«CBН-12»',
                   0.6: 'CBO0-PНо(д)0,60-R1/2/P57(68, 79, 93, 141, 182).B3-«CBН-К115»',
                   0.77: 'CBO0-PНо(д)0,77-R1/2/P57(68, 79, 93, 141, 182).B3-«CBН-15»',
                   0.84: 'CBO0-PНо(д)0,84-R1/2/P57(68, 79, 93, 141, 182).B3-«CBН-К160»',
                   1.28: 'СУS0-РНо 1,28-R3/4/Р68.В3–«СОБР-17-Н» (СУS - В – 1,28 - 68. С)',
                   1.91: 'СУS0-РНо 1,91-R1/Р93.В3–«СОБР-25-Н» (СУS - В – 1,91 - 93.С - R1)'}

def getRootDir(*args):
    if getattr(sys, 'frozen', False):
        application_path = os.path.abspath(os.path.dirname(sys.executable))
    else:
        application_path = os.path.dirname(__file__)
    if args:
        application_path = os.path.join(application_path, os.path.join(*args))
    application_path = application_path.replace('\\', '/')
    return application_path

def toLongName(path):
    '''
    from dos 8.3 format
    '''
    buf = create_unicode_buffer(500)
    windll.kernel32.GetLongPathNameW(path, buf, 500)
    return buf.value



class VyborOrositelaClass(QMainWindow, ui.Ui_mainWindow):

    def __init__(self):
        super(VyborOrositelaClass, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(os.path.join(getRootDir(), 'icon.png')))
        self.pb_raschet.clicked.connect(self.initial_data)

    def initial_data(self):
        self.kategory_VPO = self.cb_kategor_VPO.currentText()
        self.room_height = self.sb_room_height.value()
        self.storage_height = self.sb_storage_height.value()
        self.kategory = float(self.cb_kategory.currentText())
        self.area_sprinkler = self.sb_area_sprinkler.value()
        self.pressure = float(self.cb_pressure.currentText())
        self.rozetka = self.cb_rozetka.currentText()

        self.calculate()
        self.set_text()


    def calculate(self):
        intensity = self.return_intensity()
        k = self.calc_consumption(intensity, self.area_sprinkler, self.pressure)[2]
        markirovka = self.return_markirovka(k)
        self.le_markirovka.setText(markirovka)


    def return_kategory(self):
        if self.kategory == 1 or self.kategory == 2 or self.kategory == 3 or self.kategory == 4.1:
            table_kat = kat
        elif self.kategory == 5:
            table_kat = kat_5
        elif self.kategory == 6:
            table_kat = kat_6
        return table_kat

    def return_intensity(self):
        kat = self.return_kategory()
        column = self.return_column()
        if self.kategory == 1 or self.kategory == 2 or self.kategory == 3 or self.kategory == 4.1:
            row = self.return_row()
        elif self.kategory == 5 or self.kategory == 6:
            row = self.return_row_storage()
        intensity = kat[row][column]

        if self.kategory == 2 and self.kategory_VPO == 'В2':
            intensity = intensity * 1.5
        elif self.kategory == 2 and self.kategory_VPO == 'В1':
            intensity = intensity * 2.5
        return(intensity)



    def return_row(self):
        if self.kategory == 1:
            row = 0
        elif self.kategory == 2:
            row = 1
        elif self.kategory == 3:
            row = 2
        elif self.kategory == 4.1:
            row = 3
        return row

    def return_column(self):
        if self.room_height <= 10:
            column = 0
        elif 10 < self.room_height <= 12:
            column = 1
        elif 12 < self.room_height <= 14:
            column = 2
        elif 14 < self.room_height <= 16:
            column = 3
        elif 16 < self.room_height <= 18:
            column = 4
        elif 18 < self.room_height <= 20:
            column = 5
        return column

    def return_row_storage(self):
        if self.kategory == 5 or self.kategory == 6:
            if self.storage_height <= 1:
                row_storage = 0
            elif 1 < self.storage_height <= 2:
                row_storage = 1
            elif 2 < self.storage_height <= 3:
                row_storage = 2
            elif 3 < self.storage_height <= 4:
                row_storage = 3
            elif 4 < self.storage_height <= 5.5:
                row_storage = 4
            return row_storage

    def calc_consumption(self, intensity, area_sprinkler, pressure):
        consumption_tr = intensity * area_sprinkler
        for k in k_up:
            consumption_f = 10 * k * (pressure**0.5)
            if consumption_f >= consumption_tr:
                return (consumption_tr, consumption_f, k)

    def return_markirovka(self, k):
        if self.rozetka == 'Вверх':
            return markirovka_up[k]
        elif self.rozetka == 'Вниз':
            return markirovka_down[k]

    def set_text(self):
        intensity = self.return_intensity()
        consumption_tr = self.calc_consumption(intensity, self.area_sprinkler, self.pressure)[0]
        consumption_f = self.calc_consumption(intensity, self.area_sprinkler, self.pressure)[1]
        self.le_intensity.setText(str(round(intensity, 2)))
        self.le_consumption_tr.setText(str(round(consumption_tr, 2)))
        self.le_consumption_f.setText(str(round(consumption_f, 2)))

if __name__ == '__main__':
    app = QApplication([])
    w = VyborOrositelaClass()
    w.show()
    app.exec_()