import os
import sys
import time

from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt4.QtGui import QProgressBar

from GiniLorenzDialog import Ui_dlgGiniLorenz

class iniGiniLorenz(QtGui.QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ventana = Ui_dlgGiniLorenz()
        self.ventana.setupUi(self)
        self.connect(self.ventana.btnSelectCapaInput, SIGNAL("clicked()"), self.SelectCapaInput)

    def SelectCapaInput(self):
        file = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo', r'C:\Users\USUARIO\Documents\Andres\ProgramacionSIG\200918', 'Shapefile (*.shp)')
        fileInfo = QFileInfo(file)
        #self.ProgresBar()
        #layer = QgsVectorLayer(file, fileInfo.fileName(), "org")
        layer = iface.addVectorLayer(file, "Capa de entrada", "ogr")
        #QgsMapLayerRegistry.instance().addMapLayer(layer)
        self.ventana.cbxCapaInput.addItem(file)
        nF = layer.selectedFeatureCount()
        print (nF)
        #self.changeValue(50)
        '''
        layer = iface.addVectorLayer(file, "Capa de entrada", "ogr")
        if not layer:
            print "Layer failed to load!"
        try:
            options = QtGui.QFileDialog.Options() | QtGui.QFileDialog.DontUseNativeDialog
            path = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo', 'C:/', 'Text Files (*.txt)', 'Text Files (*.txt)', options)
            if path:
                #self.inter.edtTxt.setText(path)
                #print path
            else:
                QtGui.QMessageBox.critical(None, "Error", 'Debes de seleccionar un archivo',   QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        except Exception as e:
            QtGui.QMessageBox.critical(None, "Error", e,  QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

        file = QFileDialog.getOpenFileName(self. "Agregar datos de entrada", "C:/", "Shapefile(*.shp)")
        fileInfo = QFileInfo(file)
        layer = QgsVectorLayer(file, fileInfo.fileName(), "org")
        QgsMapaLayerRegistry.instance().addMapLayer(layer)
        self.ui.cbxCapaInput.addItem(layer.name())'''

    def ProgresBar(self):
        progressMessageBar = iface.messageBar().createMessage("Doing something boring...")
        progress = QProgressBar()
        progress.setMaximum(10)
        progress.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
        progressMessageBar.layout().addWidget(progress)
        iface.messageBar().pushWidget(progressMessageBar, iface.messageBar().INFO)
        for i in range(10):
            time.sleep(0.2)
            progress.setValue(i + 1)
        iface.messageBar().clearWidgets()

    def changeValue(self, value):
        layer = iface.activeLayer()
        if(layer):
            nF = layer.selectedFeatureCount()
            if (nF > 0):
                layer.startEditing()
                ob = layer.selectedFeaturesIds()
                b = QVariant(value)
                if (nF > 1):
                    for i in ob:
                        layer.changeAttributeValue(int(i), 1, b) # 1 being the second column
                else:
                    layer.changeAttributeValue(int(ob[0]), 1, b) # 1 being the second column
                layer.commitChanges()
            else:
                QtGui.QMessageBox.critical(None, "Error", 'Please select at least one feature from current layer',   QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        else:
            QtGui.QMessageBox.critical(None, "Error", 'Please select a layer',   QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)




def addVectorLayer(self, layer):
    self.LAYERS.append(layer)
    self.ventana.cbxShapeInput.addItem(layer.name(), layer)

def searchCapaInput(self):
    file = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo', r'C:\Users\HP\Escuela\Geoinformatica\7moSemestre\ProgramacionAmbienteSIG', 'Shapefile (*.shp)')
    if (len(file) > 0):
        fileInfo = QFileInfo(file)
        layer = iface.addVectorLayer(file, fileInfo.fileName(), "ogr")
        if GLfun.validateLayer(layer):
            self.addVectorLayer(layer)
            self.ventana.cbxShapeInput.setCurrentIndex(self.ventana.cbxShapeInput.count() - 1)

def capaInputSeleccionada(self, i):
    if self.ventana.cbxShapeInput.count() > 0:
        print(self.ventana.cbxShapeInput.currentText(), i)
        layer = self.LAYERS[i]
        GLfun.setFieldsInCbx(GLfun.getFieldsTypeInt(layer), self.ventana.cbxFieldData)
        GLfun.setFieldsInCbx(layer.fields(), self.ventana.cbxFieldGroup)






def getEPSG(layer):
    spc = layer.crs()
    SRC = spc.authid()
    EPSG = int(SRC[5:15])
    SRS = QgsCoordinateReferenceSystem(EPSG, QgsCoordinateReferenceSystem.EpsgCrsId)
    return SRS

def imprimir(msg):
    print(msg)
