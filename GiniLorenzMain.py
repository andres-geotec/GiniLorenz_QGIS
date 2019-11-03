import os
import sys

from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from qgis.PyQt.QtCore import QVariant

#from GiniLorenzInicio import iniGiniLorenz
from GiniLorenzDialog import Ui_dlgGiniLorenz

class giniLorenzMain:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.FMenu = QMenu(self.iface.mainWindow())
        self.FMenu.setTitle("GiniLorenz")
        self.FMenuBar = self.iface.mainWindow().menuBar()
        self.FMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(),self.FMenu)
        self.FMenuBar = self.iface.addToolBar("GiniLorenz ToolBar")

        self.objGiniLorenz = QAction(QIcon(":/plugins/GiniLorenz_02sep18/icons/icon_curva_lorenz.png"),"GiniLorenz from ITER",self.iface.mainWindow())
        self.objGiniLorenz.triggered.connect(self.showGiniLorenzWindow)
        self.FMenu.addAction(self.objGiniLorenz)

    def unload(self):
        self.iface.removePluginMenu("&GiniLorenz", self.action)

    def showGiniLorenzWindow(self):
        self.dialogo = iniGiniLorenz()
        self.dialogo.show()


import GiniLorenzFunctions as GLfun

class iniGiniLorenz(QtGui.QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ventana = Ui_dlgGiniLorenz()
        self.ventana.setupUi(self)

        vectorLayersInMap = GLfun.getVectorLayersInMap()
        if len(vectorLayersInMap) > 0:
            self.ventana.cbxShapeInput.addItems(vectorLayersInMap)
            self.ventana.cbxShapeOutput.addItems(vectorLayersInMap)
            self.shapeInputSelected()
            self.shapeOutputSelected()
        self.ventana.cbxShapeInput.currentIndexChanged.connect(self.shapeInputSelected)
        self.ventana.cbxShapeOutput.currentIndexChanged.connect(self.shapeOutputSelected)
        self.ventana.btnSearchShapeInput.clicked.connect(self.searchShapeInput)
        self.ventana.btnSearchShapeOutput.clicked.connect(self.searchShapeOutput)
        self.ventana.chkNewField.stateChanged.connect(self.chekedNewField)
        self.ventana.chkUpdateField.stateChanged.connect(self.chekedUpdateField)
        self.chekedNewField(2)
        self.ventana.btnRunMain.accepted.connect(self.validateParameters)
        self.ventana.btnRunMain.rejected.connect(self.cancelar)
        self.ventana.txtNewField.setText('GINI')

    def shapeInputSelected(self):
        layer = GLfun.getLayerByName(self.ventana.cbxShapeInput.currentText())
        GLfun.setFieldsInCbx(GLfun.getFieldsTypeInt(layer), self.ventana.cbxFieldData)
        GLfun.setFieldsInCbx(GLfun.getFieldsByTypeName(layer, 'String'), self.ventana.cbxFieldGroup)
        GLfun.setFieldsInCbx(GLfun.getFieldsByTypeName(layer, 'String'), self.ventana.cbxFieldJoinInput)

    def shapeOutputSelected(self):
        layer = GLfun.getLayerByName(self.ventana.cbxShapeOutput.currentText())
        GLfun.setFieldsInCbx(GLfun.getFieldsByTypeName(layer, 'String'), self.ventana.cbxFieldJoinOutput)
        GLfun.setFieldsInCbx(GLfun.getFieldsByTypeName(layer, 'Real'), self.ventana.cbxUpdateField)

    def searchShapeInput(self):
        pathFile = GLfun.getPathFile(self, 'Shapefile (*.shp)')
        if len(pathFile) > 0:
            self.addShapeInCbx(pathFile, self.ventana.cbxShapeInput)

    def searchShapeOutput(self):
        pathFile = GLfun.getPathFile(self, 'Shapefile (*.shp)')
        if len(pathFile) > 0:
            self.addShapeInCbx(pathFile, self.ventana.cbxShapeOutput)

    def addShapeInCbx(self, pathFile, comboBox):
        layer = GLfun.addVectorLayersInMap(pathFile)
        self.ventana.cbxShapeInput.addItem(layer.name())
        self.ventana.cbxShapeOutput.addItem(layer.name())
        comboBox.setCurrentIndex(comboBox.count() - 1)

    def chekedNewField(self, state):
        if state > 0:
            self.activeNewField()
        else:
            self.activeUpdateField()

    def chekedUpdateField(self, state):
        if state > 0:
            self.activeUpdateField()
        else:
            self.activeNewField()

    def activeNewField(self):
        self.ventana.grpNewField.setEnabled(True)
        self.ventana.cbxUpdateField.setEnabled(False)
        self.ventana.chkUpdateField.setCheckState(0)
        self.ventana.chkNewField.setCheckState(2)

    def activeUpdateField(self):
        self.ventana.cbxUpdateField.setEnabled(True)
        self.ventana.grpNewField.setEnabled(False)
        self.ventana.chkNewField.setCheckState(0)
        self.ventana.chkUpdateField.setCheckState(2)

    def validateParameters(self):
        message = True
        if self.ventana.chkNewField.checkState() == Qt.Checked:
            if GLfun.isTextEmpty(self.ventana.txtNewField.text()):
                message = 'No se asigno nombre para el nuevo campo de destino'
        else:
            if GLfun.isTextEmpty(self.ventana.cbxUpdateField.currentText()):
                message = 'No se selecciono el campo a actualizar de destino'
        if GLfun.isTextEmpty(self.ventana.cbxFieldJoinOutput.currentText()):
            message = 'No se selecciono el campo relacion de destino'
        if GLfun.isTextEmpty(self.ventana.cbxFieldJoinInput.currentText()):
            message = 'No se selecciono el campo relacion de entrada'
        if GLfun.isTextEmpty(self.ventana.cbxShapeOutput.currentText()):
            message = 'No se selecciono la capa de destino'
        if GLfun.isTextEmpty(self.ventana.cbxFieldGroup.currentText()):
            message = 'No se selecciono el campo de separacion por grupo'
        if GLfun.isTextEmpty(self.ventana.cbxFieldData.currentText()):
            message = 'No se selecciono el campo de entrada'
        if GLfun.isTextEmpty(self.ventana.cbxShapeInput.currentText()):
            message = 'No se selecciono la capa de entrada'
        if message == True:
            self.runMain()
        else:
            QtGui.QMessageBox.critical(None, "Error", message, QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

    def runMain(self):
        layer = GLfun.getLayerByName(self.ventana.cbxShapeInput.currentText())
        attributes = GLfun.getAllAttributes(layer)
        idxFieldJoinInput = layer.fieldNameIndex(self.ventana.cbxFieldJoinInput.currentText())
        idxFieldGroup = layer.fieldNameIndex(self.ventana.cbxFieldGroup.currentText())
        idxFieldData = layer.fieldNameIndex(self.ventana.cbxFieldData.currentText())
        separations = GLfun.getUniqueValues(GLfun.getValuesByField(attributes, idxFieldJoinInput))
        groups = GLfun.getUniqueValues(GLfun.getValuesByField(attributes, idxFieldGroup))
        print('\n\n' + str(len(separations)) + ' separaciones...')
        separator = {}
        for separation in separations:
            attributesBySeparation = GLfun.getAttributesByGroup(attributes, idxFieldJoinInput, separation)
            groupData = {}
            for group in groups:
                attributesByGroup = GLfun.getAttributesByGroup(attributesBySeparation, idxFieldGroup, group)
                if len(attributesByGroup) > 0:
                    #print(group + ': ' + str(len(attributesByGroup)))
                    valuesByGroup = GLfun.getValuesByField(attributesByGroup, idxFieldData)
                    groupData[group] = valuesByGroup
            print('\n\n' + separation + ': (' + str(len(attributesBySeparation)) + ' filas)  calculando....')
            gini = GLfun.getGini(groupData)
            separator[separation] = gini
            print('\nINDICE DE GINI = ' + str(gini))
        self.saveData(separator)

    def saveData(self, separator):
        print(separator)
        layer = GLfun.getLayerByName(self.ventana.cbxShapeOutput.currentText())
        nameFieldJoinOutput = self.ventana.cbxFieldJoinOutput.currentText()
        nameUpdateField = self.ventana.cbxUpdateField.currentText()
        if self.ventana.chkNewField.checkState > 0:
            nameUpdateField = self.ventana.txtNewField.text()
            if layer.dataProvider().addAttributes([QgsField(nameUpdateField, QVariant.Double)]):
                print('Se agrego un nuevo campo')
            layer.updateFields()
        idxUpdateField = layer.fieldNameIndex(nameUpdateField)

        for key in sorted( separator.keys() ):
            sentencia = (u' \"%s\" = \'%s\' ' %(nameFieldJoinOutput, key))
            print('where %s --> %f' %(sentencia, separator[key]))
            selection = layer.getFeatures(QgsFeatureRequest().setFilterExpression(sentencia))
            layer.startEditing()
            for feat in selection:
                layer.changeAttributeValue(feat.id(), idxUpdateField, separator[key])
            layer.commitChanges()


    def cancelar(self):
        print('Cancelado')
