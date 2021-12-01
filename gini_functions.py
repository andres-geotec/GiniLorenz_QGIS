# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

def gini_getPathFile(self, type):
  path, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', r'', type)
  return path

def gini_addVectorLayersInMap(pathFile):
  fileInfo = QFileInfo(pathFile)
  layer = iface.addVectorLayer(pathFile, fileInfo.fileName(), "ogr")
  return layer

def gini_getVectorLayersInMap():
  vectorLayers = []
  layers = QgsProject.instance().mapLayers().values()
  for layer in layers:
    if layer.type() == QgsMapLayer.VectorLayer:
      #if gini_validateLayer(layer):
      vectorLayers.append(layer.name())
  return vectorLayers

def validateLayer(layer):
  if layer.wkbType() != QGis.WKBLineString:
    if len(gini_getFieldsTypeInt(layer)) > 0:
      return True
  return False

def gini_getLayerByName(layerName):
  layers = QgsProject.instance().mapLayers().values()
  for layer in layers:
    if layer.name() == layerName:
      return layer

def gini_setFieldsInCbx(fields, comboBox):
  comboBox.clear()
  for field in fields:
    comboBox.addItem(field.displayName())

def gini_getFieldsTypeInt(layer):
  intFields = []
  for field in layer.fields():
    if field.isNumeric():
      intFields.append(field)
  return intFields

def gini_getFieldsByTypeName(layer, type):
  intFields = []
  for field in layer.fields():
    if field.typeName() == type:
      intFields.append(field)
  return intFields

def gini_isTextEmpty(text):
  if len(text) > 0:
    return False
  return True



#-------------------- RUN --------------------
def gini_getAllAttributes(layer):
  features = layer.dataProvider().getFeatures()
  attributes = []
  for feature in features:
    attributes.append(feature.attributes())
  return attributes