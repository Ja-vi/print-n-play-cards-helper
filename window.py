# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'central.ui'
#
# Created: Wed Jul 27 00:05:16 2016
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(909, 516)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../pfc/qtmodel/PNG/8.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 80, 591, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(290, 10, 20, 71))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 170, 591, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 10, 281, 71))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.fichero_edit = QtGui.QLineEdit(self.groupBox_2)
        self.fichero_edit.setGeometry(QtCore.QRect(10, 30, 191, 31))
        self.fichero_edit.setText(_fromUtf8(""))
        self.fichero_edit.setReadOnly(True)
        self.fichero_edit.setObjectName(_fromUtf8("fichero_edit"))
        self.elegir_boton = QtGui.QPushButton(self.groupBox_2)
        self.elegir_boton.setGeometry(QtCore.QRect(210, 30, 71, 31))
        self.elegir_boton.setObjectName(_fromUtf8("elegir_boton"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 400, 581, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.guardar_como_boton = QtGui.QPushButton(self.groupBox)
        self.guardar_como_boton.setGeometry(QtCore.QRect(500, 30, 71, 31))
        self.guardar_como_boton.setObjectName(_fromUtf8("guardar_como_boton"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 151, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.format_combo = QtGui.QComboBox(self.groupBox)
        self.format_combo.setGeometry(QtCore.QRect(330, 30, 151, 31))
        self.format_combo.setObjectName(_fromUtf8("format_combo"))
        self.format_combo.addItem(_fromUtf8(""))
        self.format_combo.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(170, 30, 151, 31))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.line_4 = QtGui.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(10, 380, 591, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(10, 260, 591, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.groupBox_9 = QtGui.QGroupBox(Form)
        self.groupBox_9.setGeometry(QtCore.QRect(20, 100, 581, 71))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.n_spin_2 = QtGui.QSpinBox(self.groupBox_9)
        self.n_spin_2.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.n_spin_2.setPrefix(_fromUtf8(""))
        self.n_spin_2.setMinimum(1)
        self.n_spin_2.setMaximum(20)
        self.n_spin_2.setObjectName(_fromUtf8("n_spin_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_9)
        self.label_2.setGeometry(QtCore.QRect(100, 40, 20, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.m_spin_2 = QtGui.QSpinBox(self.groupBox_9)
        self.m_spin_2.setGeometry(QtCore.QRect(120, 30, 71, 31))
        self.m_spin_2.setMinimum(1)
        self.m_spin_2.setMaximum(20)
        self.m_spin_2.setObjectName(_fromUtf8("m_spin_2"))
        self.dividir_boton = QtGui.QPushButton(self.groupBox_9)
        self.dividir_boton.setGeometry(QtCore.QRect(420, 30, 71, 31))
        self.dividir_boton.setObjectName(_fromUtf8("dividir_boton"))
        self.unir_boton = QtGui.QPushButton(self.groupBox_9)
        self.unir_boton.setGeometry(QtCore.QRect(500, 30, 71, 31))
        self.unir_boton.setObjectName(_fromUtf8("unir_boton"))
        self.label = QtGui.QLabel(self.groupBox_9)
        self.label.setGeometry(QtCore.QRect(200, 40, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.sep_spin = QtGui.QSpinBox(self.groupBox_9)
        self.sep_spin.setGeometry(QtCore.QRect(280, 30, 81, 31))
        self.sep_spin.setMaximum(200)
        self.sep_spin.setObjectName(_fromUtf8("sep_spin"))
        self.groupBox_8 = QtGui.QGroupBox(Form)
        self.groupBox_8.setGeometry(QtCore.QRect(620, 10, 281, 461))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.preview_label = QtGui.QLabel(self.groupBox_8)
        self.preview_label.setGeometry(QtCore.QRect(10, 30, 261, 381))
        self.preview_label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.preview_label.setFrameShadow(QtGui.QFrame.Raised)
        self.preview_label.setText(_fromUtf8(""))
        self.preview_label.setScaledContents(True)
        self.preview_label.setAlignment(QtCore.Qt.AlignCenter)
        self.preview_label.setObjectName(_fromUtf8("preview_label"))
        self.preview_slider = QtGui.QSlider(self.groupBox_8)
        self.preview_slider.setGeometry(QtCore.QRect(10, 430, 221, 20))
        self.preview_slider.setOrientation(QtCore.Qt.Horizontal)
        self.preview_slider.setObjectName(_fromUtf8("preview_slider"))
        self.borrar_boton = QtGui.QPushButton(self.groupBox_8)
        self.borrar_boton.setGeometry(QtCore.QRect(240, 420, 31, 31))
        self.borrar_boton.setObjectName(_fromUtf8("borrar_boton"))
        self.line_6 = QtGui.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(600, 10, 20, 461))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.groupBox_10 = QtGui.QGroupBox(Form)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 280, 291, 101))
        self.groupBox_10.setFlat(False)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.crop_spin = QtGui.QSpinBox(self.groupBox_10)
        self.crop_spin.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.crop_spin.setMaximum(500)
        self.crop_spin.setObjectName(_fromUtf8("crop_spin"))
        self.pushButton = QtGui.QPushButton(self.groupBox_10)
        self.pushButton.setGeometry(QtCore.QRect(100, 50, 51, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 30, 61, 21))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 50, 51, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 60, 61, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.line_9 = QtGui.QFrame(Form)
        self.line_9.setGeometry(QtCore.QRect(360, 190, 20, 71))
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 190, 251, 71))
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.border_spin = QtGui.QSpinBox(self.groupBox_5)
        self.border_spin.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.border_spin.setMinimum(1)
        self.border_spin.setMaximum(200)
        self.border_spin.setProperty("value", 30)
        self.border_spin.setObjectName(_fromUtf8("border_spin"))
        self.negro_boton = QtGui.QPushButton(self.groupBox_5)
        self.negro_boton.setGeometry(QtCore.QRect(100, 30, 71, 31))
        self.negro_boton.setObjectName(_fromUtf8("negro_boton"))
        self.blanco_boton = QtGui.QPushButton(self.groupBox_5)
        self.blanco_boton.setGeometry(QtCore.QRect(180, 30, 71, 31))
        self.blanco_boton.setObjectName(_fromUtf8("blanco_boton"))
        self.line_8 = QtGui.QFrame(Form)
        self.line_8.setGeometry(QtCore.QRect(10, 470, 901, 20))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.progress_bar = QtGui.QProgressBar(Form)
        self.progress_bar.setGeometry(QtCore.QRect(320, 490, 581, 20))
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.msg_label = QtGui.QLabel(Form)
        self.msg_label.setGeometry(QtCore.QRect(60, 490, 241, 21))
        self.msg_label.setObjectName(_fromUtf8("msg_label"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 490, 31, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.logo_button = QtGui.QPushButton(Form)
        self.logo_button.setGeometry(QtCore.QRect(20, 10, 261, 71))
        self.logo_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo_button.setIcon(icon1)
        self.logo_button.setIconSize(QtCore.QSize(260, 200))
        self.logo_button.setDefault(False)
        self.logo_button.setFlat(True)
        self.logo_button.setObjectName(_fromUtf8("logo_button"))
        self.groupBox_11 = QtGui.QGroupBox(Form)
        self.groupBox_11.setGeometry(QtCore.QRect(330, 280, 271, 101))
        self.groupBox_11.setFlat(False)
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.todas_radio = QtGui.QRadioButton(self.groupBox_11)
        self.todas_radio.setGeometry(QtCore.QRect(40, 30, 51, 26))
        self.todas_radio.setChecked(True)
        self.todas_radio.setObjectName(_fromUtf8("todas_radio"))
        self.previsualizada_radio = QtGui.QRadioButton(self.groupBox_11)
        self.previsualizada_radio.setGeometry(QtCore.QRect(140, 30, 81, 26))
        self.previsualizada_radio.setObjectName(_fromUtf8("previsualizada_radio"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_11)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 60, 251, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.quitar_boton = QtGui.QPushButton(Form)
        self.quitar_boton.setGeometry(QtCore.QRect(280, 220, 71, 31))
        self.quitar_boton.setFlat(False)
        self.quitar_boton.setObjectName(_fromUtf8("quitar_boton"))
        self.groupBox_12 = QtGui.QGroupBox(Form)
        self.groupBox_12.setGeometry(QtCore.QRect(380, 190, 221, 71))
        self.groupBox_12.setFlat(False)
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.label_4 = QtGui.QLabel(self.groupBox_12)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 41, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.umbral_spin_2 = QtGui.QSpinBox(self.groupBox_12)
        self.umbral_spin_2.setGeometry(QtCore.QRect(60, 30, 71, 31))
        self.umbral_spin_2.setMinimum(1)
        self.umbral_spin_2.setMaximum(100)
        self.umbral_spin_2.setSingleStep(5)
        self.umbral_spin_2.setProperty("value", 20)
        self.umbral_spin_2.setObjectName(_fromUtf8("umbral_spin_2"))
        self.auto_boton = QtGui.QPushButton(self.groupBox_12)
        self.auto_boton.setGeometry(QtCore.QRect(140, 30, 71, 31))
        self.auto_boton.setObjectName(_fromUtf8("auto_boton"))
        self.line_10 = QtGui.QFrame(Form)
        self.line_10.setGeometry(QtCore.QRect(310, 280, 20, 101))
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.line_11 = QtGui.QFrame(Form)
        self.line_11.setGeometry(QtCore.QRect(300, 490, 20, 21))
        self.line_11.setFrameShape(QtGui.QFrame.VLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "PnPCards", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Select Card Files (images or pdf)", None, QtGui.QApplication.UnicodeUTF8))
        self.fichero_edit.setPlaceholderText(QtGui.QApplication.translate("Form", "Elige los ficheros de origen", None, QtGui.QApplication.UnicodeUTF8))
        self.elegir_boton.setText(QtGui.QApplication.translate("Form", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Output format and size", None, QtGui.QApplication.UnicodeUTF8))
        self.guardar_como_boton.setText(QtGui.QApplication.translate("Form", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "A0", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "A1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Form", "A2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Form", "A3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Form", "A4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("Form", "A5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("Form", "A6", None, QtGui.QApplication.UnicodeUTF8))
        self.format_combo.setItemText(0, QtGui.QApplication.translate("Form", "PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.format_combo.setItemText(1, QtGui.QApplication.translate("Form", "Images", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_9.setTitle(QtGui.QApplication.translate("Form", "Specify rows, columns and interspace to split or merge the cards", None, QtGui.QApplication.UnicodeUTF8))
        self.n_spin_2.setSuffix(QtGui.QApplication.translate("Form", " row/s", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.m_spin_2.setSuffix(QtGui.QApplication.translate("Form", " col/s", None, QtGui.QApplication.UnicodeUTF8))
        self.dividir_boton.setText(QtGui.QApplication.translate("Form", "Split", None, QtGui.QApplication.UnicodeUTF8))
        self.unir_boton.setText(QtGui.QApplication.translate("Form", "Merge", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Interspace:", None, QtGui.QApplication.UnicodeUTF8))
        self.sep_spin.setSuffix(QtGui.QApplication.translate("Form", " px", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("Form", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.borrar_boton.setText(QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_10.setTitle(QtGui.QApplication.translate("Form", "Crop borders (All, to keep same size)", None, QtGui.QApplication.UnicodeUTF8))
        self.crop_spin.setSuffix(QtGui.QApplication.translate("Form", " px", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Top", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "Bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "Card border", None, QtGui.QApplication.UnicodeUTF8))
        self.border_spin.setSuffix(QtGui.QApplication.translate("Form", " px", None, QtGui.QApplication.UnicodeUTF8))
        self.negro_boton.setText(QtGui.QApplication.translate("Form", "Black", None, QtGui.QApplication.UnicodeUTF8))
        self.blanco_boton.setText(QtGui.QApplication.translate("Form", "White", None, QtGui.QApplication.UnicodeUTF8))
        self.msg_label.setText(QtGui.QApplication.translate("Form", "Ready", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Info:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_11.setTitle(QtGui.QApplication.translate("Form", "Modify all or just preview", None, QtGui.QApplication.UnicodeUTF8))
        self.todas_radio.setText(QtGui.QApplication.translate("Form", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.previsualizada_radio.setText(QtGui.QApplication.translate("Form", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "Useless decorative button", None, QtGui.QApplication.UnicodeUTF8))
        self.quitar_boton.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_12.setTitle(QtGui.QApplication.translate("Form", "Trim Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Fuzz:", None, QtGui.QApplication.UnicodeUTF8))
        self.auto_boton.setText(QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))

