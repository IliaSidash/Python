from PySide.QtCore import *
from PySide.QtGui import *
from widgets import add_in_dict_dialog_UIs as ui


class AddInDictDialog(QDialog, ui.Ui_Dialog):
    def __init__(self):
        super(AddInDictDialog, self).__init__()
        self.setupUi(self)