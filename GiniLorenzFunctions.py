from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

def getPathFile(self, type):
    path = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo', r'', type)
    return path

def addVectorLayersInMap(pathFile):
    fileInfo = QFileInfo(pathFile)
    layer = iface.addVectorLayer(pathFile, fileInfo.fileName(), "ogr")
    return layer

def getVectorLayersInMap():
    vectorLayers = []
    layers = QgsMapLayerRegistry.instance().mapLayers().values()
    for layer in layers:
        if layer.type() == QgsMapLayer.VectorLayer:
            #if validateLayer(layer):
            vectorLayers.append(layer.name())
    return vectorLayers

def validateLayer(layer):
    if layer.wkbType() != QGis.WKBLineString:
        if len(getFieldsTypeInt(layer)) > 0:
            return True
    return False

def getLayerByName(layerName):
    layers = QgsMapLayerRegistry.instance().mapLayers().values()
    for layer in layers:
        if layer.name() == layerName:
            return layer

def setFieldsInCbx(fields, comboBox):
    comboBox.clear()
    for field in fields:
        comboBox.addItem(field.displayName())

def getFieldsTypeInt(layer):
    intFields = []
    for field in layer.fields():
        if field.isNumeric():
            intFields.append(field)
    return intFields

def getFieldsByTypeName(layer, type):
    intFields = []
    for field in layer.fields():
        if field.typeName() == type:
            intFields.append(field)
    return intFields

def isTextEmpty(text):
    if len(text) > 0:
        return False
    return True



#-------------------- RUN --------------------
def getAllAttributes(layer):
    features = layer.dataProvider().getFeatures()
    attributes = []
    for feature in features:
        attributes.append(feature.attributes())
    return attributes

def getValuesByField(allAttributes, idxField):
    values = [attribute[idxField] for attribute in allAttributes]
    return values

def getUniqueValues(values):
    return sorted(set(values))

def getAttributesByGroup(allAttributes, idxFieldGroup, group):
    attributes = []
    for attribute in allAttributes:
        if attribute[idxFieldGroup] == group:
            attributes.append(attribute)
    return attributes

def getGini(dic):
    lorenzGraphicData = getLorenzGraphicData(dic)
    xyproducts = getXYProducts(lorenzGraphicData['x'], lorenzGraphicData['y'])
    print('%f,%f' %( sum( xyproducts['xproducts']), sum( xyproducts['yproducts'])) )
    coef = sum( xyproducts['xproducts']) - sum( xyproducts['yproducts'])
    while coef > 1:
        coef = coef /10
    return coef

def getLorenzGraphicData(dic):
    countTot = sum([len(dic[key]) for key in dic])
    pobTot = sum([sum(dic[key]) for key in dic])
    prAcumCount = 0
    prAcumPob = 0
    tablaLorenz = {'group':[], 'count':[], 'pob':[], 'prCount':[], 'prPob':[], 'x':[], 'y':[], 'xproduct':[], 'yproduct':[]}
    print('\n----- TABLA PARA GRAFICAR LA CURVA DE LORENZ -----')
    print('grp,cnt,pob,prCount,prPob,x,y')
    for key in sorted(dic):
        count = len(dic[key])
        pob = sum(dic[key])
        prCount = (float(count) / float(countTot)) * 100
        prPob = (float(pob) / float(pobTot)) * 100
        prAcumCount += prCount
        prAcumPob += prPob
        tablaLorenz['group'].append(key)
        tablaLorenz['count'].append(count)
        tablaLorenz['pob'].append(pob)
        tablaLorenz['prCount'].append(prCount)
        tablaLorenz['prPob'].append(prPob)
        tablaLorenz['x'].append(prAcumCount)
        tablaLorenz['y'].append(prAcumPob)
        values = (key, count, pob, prCount, prPob, prAcumCount, prAcumPob)
        print( '%s,%d,%f,%f,%f,%f,%f' %values )
    return tablaLorenz

def getXYProducts(x, y):
    xy = {'xproducts':[], 'yproducts':[]}
    print('\n----- PRODUCTOS CALCULADOS PARA OBTENER EL INDICE DE GINI -----')
    print('xproducts,yproducts')
    for i in range(len(x)):
        xproduct = 0
        yproduct = 0
        if i < (len( x ) - 1):
            xproduct = x[i] * y[i + 1]
            yproduct = x[i + 1] * y[i]
        print('%f,%f' %(xproduct, yproduct))
        xy['xproducts'].append(xproduct)
        xy['yproducts'].append(yproduct)
    return xy
