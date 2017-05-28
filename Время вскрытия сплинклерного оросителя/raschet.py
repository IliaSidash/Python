# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
import t_srabatyvania_UIs
from math import exp
from math import log
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

class t_srabatyvania(QMainWindow, t_srabatyvania_UIs.Ui_ManWindow):
    def __init__(self):
        super(t_srabatyvania, self).__init__()
        self.setupUi(self)

    # UI
        self.setWindowIcon(QIcon('I:\Python\projects\RVVSO_68/icon.png'))

    # connects
        self.pushButton.clicked.connect(self.raschet)

    def raschet(self):

        t0 = float(self.sb_t0.value())
        h = float(self.sb_horositela.value())
        nu = float(self.sb_polnota_gorenia.value())
        Qn = (float(self.sb_teplota_sgorania.value()) * 1000)
        Vl = float(self.sb_lineinai_skorost.value())
        Vud = float(self.sb_massovaia_skorost.value())
        r = float(self.sb_norm_rasstoanie.value())

        t_79 = ((h*(79-t0)*((0.7*r)**0.67))/(5.36*((3.14*nu*0.2*Qn*Vud*(Vl**2))**0.67)))**0.746
        t_110 = ((h*(110-t0)*((0.7*r)**0.67))/(5.36*((3.14*nu*0.2*Qn*Vud*(Vl**2))**0.67)))**0.746
        t_sr_79 = 1.278 * t_110 - 0.74 * t_79 + 57

        self.lb_otvet.setText('Время срабатывания спринклерного оросителя = ' + str(round(t_sr_79))
                              + ' с = ' + str(round((t_sr_79) /60, 2)) + ' мин')


if __name__ == '__main__':
    app = QApplication([])
    w = t_srabatyvania()
    w.show()
    app.exec_()