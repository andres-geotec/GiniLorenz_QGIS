import os.path
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from .clip_gini import Ui_MWClip
from .gini_functions import *

class StartDiag(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    self.ui = Ui_MWClip()
    self.ui.setupUi(self)

    vectorLayersInMap = gini_getVectorLayersInMap()
    print(vectorLayersInMap)
    if len(vectorLayersInMap) > 0:
      self.ui.cbxShapeInput.addItems(vectorLayersInMap)
      self.ui.cbxShapeOutput.addItems(vectorLayersInMap)
      self.shapeInputSelected()
      self.shapeOutputSelected()

    self.ui.cbxShapeInput.currentIndexChanged.connect(self.shapeInputSelected)
    self.ui.cbxShapeOutput.currentIndexChanged.connect(self.shapeOutputSelected)
    self.ui.btnSearchShapeInput.clicked.connect(self.searchShapeInput)
    self.ui.btnSearchShapeOutput.clicked.connect(self.searchShapeOutput)

    self.ui.chkNewField.stateChanged.connect(self.chekedNewField)
    self.ui.chkUpdateField.stateChanged.connect(self.chekedUpdateField)
    self.chekedNewField(2)

    self.ui.btnRunMain.accepted.connect(self.validateParameters)
    self.ui.btnRunMain.rejected.connect(self.cancelar)
    self.ui.txtNewField.setText('GINI')

  def shapeInputSelected(self):
    layer = gini_getLayerByName(self.ui.cbxShapeInput.currentText())
    gini_setFieldsInCbx(gini_getFieldsTypeInt(layer), self.ui.cbxFieldData)
    gini_setFieldsInCbx(gini_getFieldsByTypeName(layer, 'String'), self.ui.cbxFieldGroup)
    gini_setFieldsInCbx(gini_getFieldsByTypeName(layer, 'String'), self.ui.cbxFieldJoinInput)
  
  def shapeOutputSelected(self):
    layer = gini_getLayerByName(self.ui.cbxShapeOutput.currentText())
    gini_setFieldsInCbx(gini_getFieldsByTypeName(layer, 'String'), self.ui.cbxFieldJoinOutput)
    gini_setFieldsInCbx(gini_getFieldsByTypeName(layer, 'Real'), self.ui.cbxUpdateField)

  def searchShapeInput(self):
    pathFile = gini_getPathFile(self, 'Shapefile (*.shp)')
    if pathFile!='':
      self.addShapeInCbx(pathFile, self.ui.cbxShapeInput)
  
  def shapeOutputSelected(self):
    layer = gini_getLayerByName(self.ui.cbxShapeOutput.currentText())
    gini_setFieldsInCbx(gini_getFieldsByTypeName(layer, 'String'), self.ui.cbxFieldJoinOutput)
    gini_setFieldsInCbx(gini_getFieldsByTypeName(layer, 'Real'), self.ui.cbxUpdateField)
  
  def searchShapeOutput(self):
    pathFile = gini_getPathFile(self, 'Shapefile (*.shp)')
    if len(pathFile) > 0:
      self.addShapeInCbx(pathFile, self.ui.cbxShapeOutput)

  def addShapeInCbx(self, pathFile, comboBox):
    layer = gini_addVectorLayersInMap(pathFile)
    self.ui.cbxShapeInput.addItem(layer.name())
    self.ui.cbxShapeOutput.addItem(layer.name())
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
    self.ui.grpNewField.setEnabled(True)
    self.ui.cbxUpdateField.setEnabled(False)
    self.ui.chkUpdateField.setCheckState(0)
    self.ui.chkNewField.setCheckState(2)

  def activeUpdateField(self):
    self.ui.cbxUpdateField.setEnabled(True)
    self.ui.grpNewField.setEnabled(False)
    self.ui.chkNewField.setCheckState(0)
    self.ui.chkUpdateField.setCheckState(2)
  
  def validateParameters(self):
    message = True
    if self.ui.chkNewField.checkState() == Qt.Checked:
      if gini_isTextEmpty(self.ui.txtNewField.text()):
        message = 'No se asigno nombre para el nuevo campo de destino'
    else:
      if gini_isTextEmpty(self.ui.cbxUpdateField.currentText()):
        message = 'No se selecciono el campo a actualizar de destino'
    
    if gini_isTextEmpty(self.ui.cbxFieldJoinOutput.currentText()):
      message = 'No se selecciono el campo relacion de destino'
    if gini_isTextEmpty(self.ui.cbxFieldJoinInput.currentText()):
      message = 'No se selecciono el campo relacion de entrada'
    if gini_isTextEmpty(self.ui.cbxShapeOutput.currentText()):
      message = 'No se selecciono la capa de destino'
    if gini_isTextEmpty(self.ui.cbxFieldGroup.currentText()):
      message = 'No se selecciono el campo de separacion por grupo'
    if gini_isTextEmpty(self.ui.cbxFieldData.currentText()):
      message = 'No se selecciono el campo de entrada'
    if gini_isTextEmpty(self.ui.cbxShapeInput.currentText()):
      message = 'No se selecciono la capa de entrada'

    if message == True:
      self.runMain()
    else:
      QMessageBox.critical(None, "Error", message, QMessageBox.Ok, QMessageBox.Ok)
  
  def runMain(self):
    print('INICIANDO...')
    layer = gini_getLayerByName(self.ui.cbxShapeInput.currentText())
    attributes = gini_getAllAttributes(layer)
    idxFieldJoinInput = layer.dataProvider().fieldNameIndex(self.ui.cbxFieldJoinInput.currentText())
    idxFieldGroup = layer.dataProvider().fieldNameIndex(self.ui.cbxFieldGroup.currentText())
    idxFieldData = layer.dataProvider().fieldNameIndex(self.ui.cbxFieldData.currentText())

    separations = gini_getUniqueValues(gini_getValuesByField(attributes, idxFieldJoinInput))
    groups = gini_getUniqueValues(gini_getValuesByField(attributes, idxFieldGroup))
    print('\n\n' + str(len(separations)) + ' separaciones...')

    separator = {}
    for separation in separations:
      attributesBySeparation = gini_getAttributesByGroup(attributes, idxFieldJoinInput, separation)
      groupData = {}
      for group in groups:
        attributesByGroup = gini_getAttributesByGroup(attributesBySeparation, idxFieldGroup, group)
        if len(attributesByGroup) > 0:
          #print(group + ': ' + str(len(attributesByGroup)))
          valuesByGroup = gini_getValuesByField(attributesByGroup, idxFieldData)
          groupData[group] = valuesByGroup
      print('\n\n' + separation + ': (' + str(len(attributesBySeparation)) + ' filas)  calculando....')
      gini = gini_getGini(groupData)
      separator[separation] = gini
      print('\nINDICE DE GINI = ' + str(gini))
    self.saveData(separator)

  def saveData(self, separator):
    print(separator)
    layer = gini_getLayerByName(self.ui.cbxShapeOutput.currentText())
    nameFieldJoinOutput = self.ui.cbxFieldJoinOutput.currentText()
    nameUpdateField = self.ui.cbxUpdateField.currentText()
    print(self.ui.chkNewField.checkState(), self.ui.chkUpdateField.checkState())
    if self.ui.chkNewField.checkState() > 0:
      nameUpdateField = self.ui.txtNewField.text()
      if layer.dataProvider().addAttributes([QgsField(nameUpdateField, QVariant.Double)]):
        print('Se agrego un nuevo campo')
      layer.updateFields()
    #idxUpdateField = layer.dataProvider().fieldNameIndex(nameUpdateField)

    layer.startEditing()
    for key in sorted( separator.keys() ):
      sentencia = (u' \"%s\" = \'%s\' ' %(nameFieldJoinOutput, key))
      print('where %s --> %f' %(sentencia, separator[key]))
      layer.selectByExpression(sentencia, QgsVectorLayer.SetSelection)
      #selection = layer.dataProvider().getFeatures(QgsFeatureRequest().setFilterExpression(sentencia))
      featureSeleccionado = layer.selectedFeatures()[0]
      featureSeleccionado[nameUpdateField] = 0
      layer.updateFeature(featureSeleccionado)
      layer.commitChanges()
      layer.removeSelection()
    iface.mapCanvas().refresh()

  def cancelar(self):
    print('Cancelado')