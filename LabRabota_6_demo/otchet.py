from PySide.QtGui import *

from widgets import widgetOtchet_UIs as ui


class otchetClass(QWidget, ui.Ui_Form):
    def __init__(self, name):
        super(otchetClass, self).__init__()
        self.setupUi(self)
        name = name + '.txt'
        with open(name, 'r', encoding='utf-8') as f:
            a = f.read()
            self.lb_otchet.setText(a)