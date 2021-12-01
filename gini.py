import os.path
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from .gini_dialog import StartDiag

class Gini:
  def __init__(self, iface):
    self.iface = iface

  def initGui(self):
    self.layerMenu = QMenu(self.iface.mainWindow())
    self.layerMenu.setTitle("GiniLorenz")
    self.layerMenuBar = self.iface.mainWindow().menuBar()
    self.layerMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.layerMenu)
    self.layerMenuBar = self.iface.addToolBar("GiniLorenz ToolBar")
    
    self.ejemploLayer = QAction(QIcon(":/plugins/GiniLorenz_02sep18/icons/icon_curva_lorenz.png"),"GiniLorenz",self.iface.mainWindow())
    self.ejemploLayer.triggered.connect(self.Startdialogo)
    self.layerMenu.addAction(self.ejemploLayer)

  def Startdialogo(self):
    self.dialogo = StartDiag()
    self.dialogo.show()