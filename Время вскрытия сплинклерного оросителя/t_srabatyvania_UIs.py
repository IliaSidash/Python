# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\operator.TEACHER\Dropbox\Programming\Python\projects\RVVSO_79\t_srabatyvania.ui'
#
# Created: Thu Apr  6 14:20:54 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ManWindow(object):
    def setupUi(self, ManWindow):
        ManWindow.setObjectName("ManWindow")
        ManWindow.resize(550, 396)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ManWindow.sizePolicy().hasHeightForWidth())
        ManWindow.setSizePolicy(sizePolicy)
        ManWindow.setMinimumSize(QtCore.QSize(550, 385))
        ManWindow.setMaximumSize(QtCore.QSize(550, 396))
        self.centralwidget = QtGui.QWidget(ManWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sb_t0 = QtGui.QDoubleSpinBox(self.groupBox)
        self.sb_t0.setMaximumSize(QtCore.QSize(110, 16777215))
        self.sb_t0.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sb_t0.setMaximum(9999.99)
        self.sb_t0.setProperty("value", 20.0)
        self.sb_t0.setObjectName("sb_t0")
        self.gridLayout_2.addWidget(self.sb_t0, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.sb_horositela = QtGui.QDoubleSpinBox(self.groupBox)
        self.sb_horositela.setMaximumSize(QtCore.QSize(110, 16777215))
        self.sb_horositela.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sb_horositela.setMaximum(6.0)
        self.sb_horositela.setSingleStep(0.1)
        self.sb_horositela.setProperty("value", 5.5)
        self.sb_horositela.setObjectName("sb_horositela")
        self.gridLayout_2.addWidget(self.sb_horositela, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 5, 0, 1, 2)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.sb_teplota_sgorania = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.sb_teplota_sgorania.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sb_teplota_sgorania.setDecimals(2)
        self.sb_teplota_sgorania.setMaximum(1000.0)
        self.sb_teplota_sgorania.setProperty("value", 16.72)
        self.sb_teplota_sgorania.setObjectName("sb_teplota_sgorania")
        self.gridLayout_3.addWidget(self.sb_teplota_sgorania, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.sb_massovaia_skorost = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.sb_massovaia_skorost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sb_massovaia_skorost.setDecimals(2)
        self.sb_massovaia_skorost.setSingleStep(0.01)
        self.sb_massovaia_skorost.setProperty("value", 0.01)
        self.sb_massovaia_skorost.setObjectName("sb_massovaia_skorost")
        self.gridLayout_3.addWidget(self.sb_massovaia_skorost, 4, 1, 1, 1)
        self.sb_norm_rasstoanie = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.sb_norm_rasstoanie.setMinimumSize(QtCore.QSize(9, 0))
        self.sb_norm_rasstoanie.setMaximumSize(QtCore.QSize(110, 16777215))
        self.sb_norm_rasstoanie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sb_norm_rasstoanie.setDecimals(1)
        self.sb_norm_rasstoanie.setSingleStep(0.1)
        self.sb_norm_rasstoanie.setProperty("value", 4.0)
        self.sb_norm_rasstoanie.setObjectName("sb_norm_rasstoanie")
        self.gridLayout_3.addWidget(self.sb_norm_rasstoanie, 0, 1, 1, 1)
        self.sb_lineinai_skorost = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.sb_lineinai_skorost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sb_lineinai_skorost.setDecimals(3)
        self.sb_lineinai_skorost.setSingleStep(0.001)
        self.sb_lineinai_skorost.setProperty("value", 0.006)
        self.sb_lineinai_skorost.setObjectName("sb_lineinai_skorost")
        self.gridLayout_3.addWidget(self.sb_lineinai_skorost, 3, 1, 1, 1)
        self.sb_polnota_gorenia = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.sb_polnota_gorenia.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sb_polnota_gorenia.setSingleStep(0.05)
        self.sb_polnota_gorenia.setProperty("value", 0.95)
        self.sb_polnota_gorenia.setObjectName("sb_polnota_gorenia")
        self.gridLayout_3.addWidget(self.sb_polnota_gorenia, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lb_otvet = QtGui.QLabel(self.groupBox_3)
        self.lb_otvet.setObjectName("lb_otvet")
        self.verticalLayout_5.addWidget(self.lb_otvet)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        ManWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(ManWindow)
        self.statusbar.setObjectName("statusbar")
        ManWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(ManWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menuBar.setObjectName("menuBar")
        ManWindow.setMenuBar(self.menuBar)
        self.action = QtGui.QAction(ManWindow)
        self.action.setObjectName("action")

        self.retranslateUi(ManWindow)
        QtCore.QMetaObject.connectSlotsByName(ManWindow)

    def retranslateUi(self, ManWindow):
        ManWindow.setWindowTitle(QtGui.QApplication.translate("ManWindow", "Время вскрытия спринклерного оросителя с учетом инерционности", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ManWindow", "Исходные данные для расчета", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ManWindow", "Температура в помещении, *С", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ManWindow", "Высота размещения оросителя, м", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ManWindow", "Характеристика пожарной нагрузки", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ManWindow", "Удельная массовая скорость выгорания горючей нагрузки,кг*м-2*с-1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ManWindow", "Низшая теплота сгорания материала, МДж/кг", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ManWindow", "Расчитать", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ManWindow", "Коэффициент полноты горения", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ManWindow", "Линейная скорость распространения пламени, м*с-1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ManWindow", "Нормативное расстояние между оросителями, м", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ManWindow", "Результаты расчета", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_otvet.setText(QtGui.QApplication.translate("ManWindow", "Время срабатывания спринклерного оросителя:", None, QtGui.QApplication.UnicodeUTF8))
        self.action.setText(QtGui.QApplication.translate("ManWindow", "Вызов справки", None, QtGui.QApplication.UnicodeUTF8))

