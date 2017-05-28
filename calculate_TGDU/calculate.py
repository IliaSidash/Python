from PySide.QtCore import *
from PySide.QtGui import *
from widgets import main_window_UIs as ui
from widgets import about_programm_dial as dial
import math, root_dir, ctypes, os
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

class CalculateTgdu(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(CalculateTgdu, self).__init__()
        self.setupUi(self)

    # UI
        self.setWindowIcon(QIcon(root_dir.get_icon()))
        self.lb_fig1.setPixmap(os.path.join(root_dir.getRootDir(), 'fig/fig1.png'))
        self.lb_fig2.setPixmap(os.path.join(root_dir.getRootDir(), 'fig/fig2.png'))
        self.lb_fig3.setPixmap(os.path.join(root_dir.getRootDir(), 'fig/fig3.png'))

    # connect
        self.pb_start.clicked.connect(self.calculate_tgdu)
        self.checkBox.clicked.connect(self.visible_element)
        self.checkBox_2.clicked.connect(self.visible_element)
        self.pb_del.clicked.connect(self.clear_all)
        self.action.triggered.connect(self.about_programm)
        self.dsb_length.valueChanged.connect(self.set_text_volume_rgs)
        self.dsb_diam.valueChanged.connect(self.set_text_volume_rgs)
        self.dsb_level.valueChanged.connect(self.set_text_volume)

    def set_text_volume_rgs(self):
        diam = self.dsb_diam.value()
        length = self.dsb_length.value()
        self.le_volume.setText(str(round((3.14 * ((diam / 2) ** 2) * length), 2)))

    def set_text_volume(self):
        diam = self.dsb_diam.value()
        length = self.dsb_length.value()
        level = self.dsb_level.value()
        if level == 0:
            self.le_volume2.setText('0')
            self.le_volume_proc.setText('0')
        elif 0 < level < (diam / 2):
            volume_np = self.area(diam, level) * length
            self.le_volume2.setText(str(round(volume_np, 2)))
            self.le_volume_proc.setText(str(round(volume_np / self.volume_rgs(diam, length) * 100, 0)))
        elif level == (diam / 2):
            volume_np = self.area(diam, level) * length
            self.le_volume2.setText(str(round(volume_np, 2)))
            self.le_volume_proc.setText(str(round(volume_np / self.volume_rgs(diam, length) * 100, 0)))
        elif diam > level > (diam / 2):
            self.le_volume2.setText('')
            self.le_volume_proc.setText('')
        elif level == diam:
            volume_np = self.volume_rgs(diam, length)
            self.le_volume2.setText(str(round(volume_np, 2)))
            self.le_volume_proc.setText(str(round(volume_np / self.volume_rgs(diam, length) * 100, 0)))
        elif level > diam:
            self.le_volume2.setText('0')
            self.le_volume_proc.setText('0')


    def about_programm(self):
        self.dial = dial.AboutProgrammDial()
        self.dial.exec_()

    def clear_all(self):
        self.dsb_diam.setValue(0)
        self.dsb_length.setValue(0)
        self.le_volume.setText('')
        self.dsb_level.setValue(0)
        self.le_volume2.setText('')
        self.le_volume_proc.setText('')
        self.sb_quantity.setValue(0)
        self.le_one_rgs.setText('')
        self.le_some_rgs.setText('')
        self.le_all_quantity.setText('')

    def visible_element(self):
        if self.checkBox.isChecked():
            self.label_11.setVisible(True)
            self.sb_quantity.setVisible(True)
            self.label_17.setVisible(True)
            self.le_some_rgs.setVisible(True)
        else:
            self.label_11.setVisible(False)
            self.sb_quantity.setVisible(False)
            self.label_17.setVisible(False)
            self.le_some_rgs.setVisible(False)
        if self.checkBox_2.isChecked():
            self.label_13.setVisible(True)
            self.label_14.setVisible(True)
            self.label_18.setVisible(True)
            self.sb_time.setVisible(True)
            self.comboBox.setVisible(True)
            self.le_all_quantity.setVisible(True)
        else:
            self.label_13.setVisible(False)
            self.label_14.setVisible(False)
            self.sb_time.setVisible(False)
            self.comboBox.setVisible(False)
            self.label_18.setVisible(False)
            self.le_all_quantity.setVisible(False)


    def initial_data(self):
        diametr = self.dsb_diam.value()
        length = self.dsb_length.value()
        overflow_level = self.dsb_level.value()
        data = (diametr, length, overflow_level)
        return data

    def calculate_tgdu(self):
        data = self.initial_data()
        if data[2] == 0:
            self.set_text(2.26 * self.volume_rgs(data[0], data[1]))

        elif 0 < data[2] < (data[0]/2):
            self.set_text(2.23 * (self.volume_rgs(data[0], data[1]) - (self.area(data[0], data[2]) * data[1])))

        elif data[2] == (data[0]/2):
            self.set_text(2.2 * (0.5 * self.volume_rgs(data[0], data[1])))

        elif data[0] > data[2] > (data[0]/2):
            volume_np = self.volume_rgs(data[0], data[1]) -  self.area(data[0], (data[0]-data[2])) * data[1]
            self.le_volume2.setText(str(round(volume_np, 2)))
            self.le_volume_proc.setText(str(round(volume_np / self.volume_rgs(data[0], data[1]) * 100, 0)))
            self.set_text(2.17 * (self.area(data[0], (data[0]-data[2])) * data[1]))

        elif data[2] == data[0]:
            self.set_text(2.17 * (self.area(data[0], (data[0] - data[2])) * data[1]))



    def set_text(self, tgdu):
        self.le_one_rgs.setText(str(round(tgdu, 2)))
        if self.checkBox.isChecked():
            quantity = self.sb_quantity.value()
            self.le_some_rgs.setText(str(round((quantity * tgdu), 2)))

        if self.checkBox_2.isChecked():
            increase_tuple = ((1.096, 1.092, 1.083), (1.179, 1.164, 1.143), (1.258, 1.223, 1.2))
            time = self.sb_time.value()
            period_index = self.comboBox.currentIndex()
            self.le_all_quantity.setText(str(round((increase_tuple[time-1][period_index] * quantity * tgdu), 2)))


    def volume_rgs(self, diam, length):
        return 3.14 * ((diam/2)**2) * length

    def area(self, diam, level):
        triangle_side = 2 * math.sqrt(((diam / 2) ** 2) - (((diam / 2) - level) ** 2))
        semiperimetr = (diam + triangle_side) / 2
        triangle_area = math.sqrt(semiperimetr * (semiperimetr - (diam / 2)) * (semiperimetr - (diam / 2)) * (semiperimetr - triangle_side))
        sector_area = ((2 * math.acos((diam/2 - level) / (diam/2))) * ((diam/2)**2)) / 2
        return sector_area - triangle_area

if __name__ == '__main__':
    app = QApplication([])
    w = CalculateTgdu()
    w.show()
    app.exec_()

