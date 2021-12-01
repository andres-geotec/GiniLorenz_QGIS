import os.path
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from .clip_gini import Ui_MWClip

class StartDiag (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MWClip()
        self.ui.setupUi(self)