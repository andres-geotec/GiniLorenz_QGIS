# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GiniLorenzDialog.ui'
#
# Created: Mon Nov 26 00:20:42 2018
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dlgGiniLorenz(object):
    def setupUi(self, dlgGiniLorenz):
        dlgGiniLorenz.setObjectName(_fromUtf8("dlgGiniLorenz"))
        dlgGiniLorenz.resize(800, 450)
        dlgGiniLorenz.setMinimumSize(QtCore.QSize(800, 450))
        dlgGiniLorenz.setMaximumSize(QtCore.QSize(800, 450))
        dlgGiniLorenz.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GiniLorenz_02sep18/icons/icon_curva_lorenz.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgGiniLorenz.setWindowIcon(icon)

        self.groupBox = QtGui.QGroupBox(dlgGiniLorenz)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 450, 130))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cbxShapeInput = QtGui.QComboBox(self.groupBox)
        self.cbxShapeInput.setGeometry(QtCore.QRect(10, 40, 390, 20))
        self.cbxShapeInput.setObjectName(_fromUtf8("cbxShapeInput"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 200, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.btnSearchShapeInput = QtGui.QPushButton(self.groupBox)
        self.btnSearchShapeInput.setGeometry(QtCore.QRect(410, 40, 30, 20))
        self.btnSearchShapeInput.setObjectName(_fromUtf8("btnSearchShapeInput"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 200, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cbxFieldData = QtGui.QComboBox(self.groupBox)
        self.cbxFieldData.setGeometry(QtCore.QRect(220, 70, 220, 20))
        self.cbxFieldData.setObjectName(_fromUtf8("cbxFieldData"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 200, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cbxFieldGroup = QtGui.QComboBox(self.groupBox)
        self.cbxFieldGroup.setGeometry(QtCore.QRect(220, 100, 220, 20))
        self.cbxFieldGroup.setObjectName(_fromUtf8("cbxFieldGroup"))

        self.groupBox_2 = QtGui.QGroupBox(dlgGiniLorenz)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 450, 70))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 200, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cbxShapeOutput = QtGui.QComboBox(self.groupBox_2)
        self.cbxShapeOutput.setGeometry(QtCore.QRect(10, 40, 390, 20))
        self.cbxShapeOutput.setObjectName(_fromUtf8("cbxShapeOutput"))
        self.btnSearchShapeOutput = QtGui.QToolButton(self.groupBox_2)
        self.btnSearchShapeOutput.setGeometry(QtCore.QRect(410, 40, 30, 20))
        self.btnSearchShapeOutput.setObjectName(_fromUtf8("btnSearchShapeOutput"))

        self.groupBox_3 = QtGui.QGroupBox(dlgGiniLorenz)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 230, 450, 80))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 200, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 200, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.cbxFieldJoinInput = QtGui.QComboBox(self.groupBox_3)
        self.cbxFieldJoinInput.setGeometry(QtCore.QRect(220, 20, 220, 20))
        self.cbxFieldJoinInput.setObjectName(_fromUtf8("cbxFieldJoinInput"))
        self.cbxFieldJoinOutput = QtGui.QComboBox(self.groupBox_3)
        self.cbxFieldJoinOutput.setGeometry(QtCore.QRect(220, 50, 220, 20))
        self.cbxFieldJoinOutput.setObjectName(_fromUtf8("cbxFieldJoinOutput"))

        self.groupBox_4 = QtGui.QGroupBox(dlgGiniLorenz)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 320, 450, 80))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.chkNewField = QtGui.QCheckBox(self.groupBox_4)
        self.chkNewField.setGeometry(QtCore.QRect(10, 20, 200, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkNewField.setFont(font)
        self.chkNewField.setObjectName(_fromUtf8("chkNewField"))
        self.chkUpdateField = QtGui.QCheckBox(self.groupBox_4)
        self.chkUpdateField.setGeometry(QtCore.QRect(10, 50, 200, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkUpdateField.setFont(font)
        self.chkUpdateField.setObjectName(_fromUtf8("chkUpdateField"))
        self.cbxUpdateField = QtGui.QComboBox(self.groupBox_4)
        self.cbxUpdateField.setGeometry(QtCore.QRect(220, 50, 220, 20))
        self.cbxUpdateField.setObjectName(_fromUtf8("cbxUpdateField"))
        self.grpNewField = QtGui.QGroupBox(self.groupBox_4)
        self.grpNewField.setGeometry(QtCore.QRect(220, 20, 220, 20))
        self.grpNewField.setTitle(_fromUtf8(""))
        self.grpNewField.setObjectName(_fromUtf8("grpNewField"))
        self.label_7 = QtGui.QLabel(self.grpNewField)
        self.label_7.setGeometry(QtCore.QRect(5, 0, 50, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.txtNewField = QtGui.QLineEdit(self.grpNewField)
        self.txtNewField.setGeometry(QtCore.QRect(60, 0, 160, 20))
        self.txtNewField.setObjectName(_fromUtf8("txtNewField"))

        self.prgProgresBarMain = QtGui.QProgressBar(dlgGiniLorenz)
        self.prgProgresBarMain.setGeometry(QtCore.QRect(170, 410, 620, 30))
        self.prgProgresBarMain.setProperty("value", 0)
        self.prgProgresBarMain.setObjectName(_fromUtf8("prgProgresBarMain"))

        self.btnRunMain = QtGui.QDialogButtonBox(dlgGiniLorenz)
        self.btnRunMain.setGeometry(QtCore.QRect(10, 410, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRunMain.setFont(font)
        self.btnRunMain.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnRunMain.setCenterButtons(True)
        self.btnRunMain.setObjectName(_fromUtf8("btnRunMain"))

        self.graphicsViewMain = QtGui.QGraphicsView(dlgGiniLorenz)
        self.graphicsViewMain.setGeometry(QtCore.QRect(470, 10, 320, 390))
        self.graphicsViewMain.setObjectName(_fromUtf8("graphicsViewMain"))

        self.retranslateUi(dlgGiniLorenz)
        QtCore.QMetaObject.connectSlotsByName(dlgGiniLorenz)

    def retranslateUi(self, dlgGiniLorenz):
        dlgGiniLorenz.setWindowTitle(_translate("dlgGiniLorenz", "GiniLorenz from ITER", None))
        self.groupBox.setTitle(_translate("dlgGiniLorenz", "Parámetros de entrada", None))
        self.label.setText(_translate("dlgGiniLorenz", "Selecciona el shape con datos:", None))
        self.btnSearchShapeInput.setText(_translate("dlgGiniLorenz", "...", None))
        self.label_2.setText(_translate("dlgGiniLorenz", "Campo de entrada (poblacion):", None))
        self.label_3.setText(_translate("dlgGiniLorenz", "Campo de separación por grupo:", None))
        
        self.groupBox_2.setTitle(_translate("dlgGiniLorenz", "Guardar datos en...", None))
        self.label_4.setText(_translate("dlgGiniLorenz", "Selecciona el shape destino:", None))
        self.btnSearchShapeOutput.setText(_translate("dlgGiniLorenz", "...", None))
        
        self.groupBox_3.setTitle(_translate("dlgGiniLorenz", "Relacionar datos por:", None))
        self.label_5.setText(_translate("dlgGiniLorenz", "Campo 1 (capa de entrada):", None))
        self.label_6.setText(_translate("dlgGiniLorenz", "Campo 2 (capa de destino):", None))
        
        self.groupBox_4.setTitle(_translate("dlgGiniLorenz", "Resultado (capa destino)", None))
        self.chkNewField.setText(_translate("dlgGiniLorenz", "Crear campo nuevo (decimal): ", None))
        self.chkUpdateField.setText(_translate("dlgGiniLorenz", "Actualizar capo existente:", None))
        self.label_7.setText(_translate("dlgGiniLorenz", "Nombre:", None))

import resources_rc
