# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\operator.TEACHER\Dropbox\Programming\Python\projects\Calculate_rezervuar\widgets\main_window.ui'
#
# Created: Tue May 16 13:36:38 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 698)
        MainWindow.setMinimumSize(QtCore.QSize(539, 0))
        MainWindow.setMaximumSize(QtCore.QSize(540, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(540, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(540, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.le_some_rgs = QtGui.QLineEdit(self.centralwidget)
        self.le_some_rgs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_some_rgs.setObjectName("le_some_rgs")
        self.gridLayout.addWidget(self.le_some_rgs, 22, 3, 1, 1)
        self.dsb_diam = QtGui.QDoubleSpinBox(self.centralwidget)
        self.dsb_diam.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsb_diam.setObjectName("dsb_diam")
        self.gridLayout.addWidget(self.dsb_diam, 2, 3, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 6, 0, 1, 4)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 2)
        self.dsb_length = QtGui.QDoubleSpinBox(self.centralwidget)
        self.dsb_length.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsb_length.setObjectName("dsb_length")
        self.gridLayout.addWidget(self.dsb_length, 3, 3, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 17, 0, 1, 4)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 13, 0, 1, 4)
        self.le_volume_proc = QtGui.QLineEdit(self.centralwidget)
        self.le_volume_proc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_volume_proc.setObjectName("le_volume_proc")
        self.gridLayout.addWidget(self.le_volume_proc, 9, 3, 1, 1)
        self.le_volume2 = QtGui.QLineEdit(self.centralwidget)
        self.le_volume2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_volume2.setObjectName("le_volume2")
        self.gridLayout.addWidget(self.le_volume2, 8, 3, 1, 1)
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 20, 0, 1, 4)
        self.le_volume = QtGui.QLineEdit(self.centralwidget)
        self.le_volume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_volume.setObjectName("le_volume")
        self.gridLayout.addWidget(self.le_volume, 4, 3, 1, 1)
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 22, 0, 1, 3)
        self.sb_time = QtGui.QSpinBox(self.centralwidget)
        self.sb_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sb_time.setMinimum(1)
        self.sb_time.setMaximum(3)
        self.sb_time.setObjectName("sb_time")
        self.gridLayout.addWidget(self.sb_time, 14, 3, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 19, 0, 1, 4)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 15, 3, 1, 1)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 15, 2, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 14, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 24, 0, 1, 4)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 2, 1, 1)
        self.pb_del = QtGui.QPushButton(self.centralwidget)
        self.pb_del.setObjectName("pb_del")
        self.gridLayout.addWidget(self.pb_del, 18, 2, 1, 2)
        self.pb_start = QtGui.QPushButton(self.centralwidget)
        self.pb_start.setObjectName("pb_start")
        self.gridLayout.addWidget(self.pb_start, 18, 0, 1, 2)
        self.lb_fig2 = QtGui.QLabel(self.centralwidget)
        self.lb_fig2.setText("")
        self.lb_fig2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_fig2.setObjectName("lb_fig2")
        self.gridLayout.addWidget(self.lb_fig2, 8, 0, 3, 2)
        self.le_one_rgs = QtGui.QLineEdit(self.centralwidget)
        self.le_one_rgs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_one_rgs.setObjectName("le_one_rgs")
        self.gridLayout.addWidget(self.le_one_rgs, 21, 3, 1, 1)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 14, 2, 1, 1)
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 23, 0, 1, 3)
        self.lb_fig1 = QtGui.QLabel(self.centralwidget)
        self.lb_fig1.setText("")
        self.lb_fig1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_fig1.setObjectName("lb_fig1")
        self.gridLayout.addWidget(self.lb_fig1, 3, 0, 3, 2)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 12, 2, 1, 1)
        self.sb_quantity = QtGui.QSpinBox(self.centralwidget)
        self.sb_quantity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sb_quantity.setMinimum(1)
        self.sb_quantity.setObjectName("sb_quantity")
        self.gridLayout.addWidget(self.sb_quantity, 12, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 11, 0, 1, 4)
        self.le_all_quantity = QtGui.QLineEdit(self.centralwidget)
        self.le_all_quantity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_all_quantity.setObjectName("le_all_quantity")
        self.gridLayout.addWidget(self.le_all_quantity, 23, 3, 1, 1)
        self.dsb_level = QtGui.QDoubleSpinBox(self.centralwidget)
        self.dsb_level.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsb_level.setObjectName("dsb_level")
        self.gridLayout.addWidget(self.dsb_level, 7, 3, 1, 1)
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 21, 0, 1, 3)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setText("Запас ТГДУ при потерях от испарения в случае длительного хранения в термоконтейнерах:  ")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setScaledContents(False)
        self.label_12.setWordWrap(True)
        self.label_12.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 14, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 12, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 10, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 16, 3, 1, 1)
        self.lb_fig3 = QtGui.QLabel(self.centralwidget)
        self.lb_fig3.setText("")
        self.lb_fig3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_fig3.setObjectName("lb_fig3")
        self.gridLayout.addWidget(self.lb_fig3, 15, 0, 2, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setSeparatorsCollapsible(True)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.label_11.setVisible(False)
        self.sb_quantity.setVisible(False)
        self.label_13.setVisible(False)
        self.sb_time.setVisible(False)
        self.label_14.setVisible(False)
        self.comboBox.setVisible(False)
        self.label_17.setVisible(False)
        self.label_18.setVisible(False)
        self.le_some_rgs.setVisible(False)
        self.le_all_quantity.setVisible(False)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Запас \"ТГДУ-РГС\" ver. 1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Количество нефтепродукта в РГС:          ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "- уровень взлива h, м", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Исходные данные для расчета", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Требуемое количество ТГДУ для флегматизации нескольких РГС, кг", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Количество РГС подлежащих флегматизации: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "- объем куб. м", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "Результаты расчета", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "теплый", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "переходный", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "холодный", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "- период года: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "- длина L, м", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Характеристика РГС:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "- относительный объем, %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "- объем, куб. м", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_del.setText(QtGui.QApplication.translate("MainWindow", "Очистить", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_start.setText(QtGui.QApplication.translate("MainWindow", "Пуск", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "- предполагаемый срок хранения гранулированного льда (от 1 до 3-х суток), сут", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Общее количество ТГДУ с учетом запаса при потерях от испарения, кг", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "- количество РГС, шт", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "- диаметр D, м", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Требуемое количество ТГДУ для флегматизации одного РГС, кг", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "Справка", None, QtGui.QApplication.UnicodeUTF8))
        self.action.setText(QtGui.QApplication.translate("MainWindow", "О программе", None, QtGui.QApplication.UnicodeUTF8))

