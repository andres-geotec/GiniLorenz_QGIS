def category():
  return "andres-gotec"
    
def classFactory(iface):
  from .gini import Gini
  return Gini(iface)

'''
def classFactory (iface):
    from GiniLorenzMain import giniLorenzMain
    return giniLorenzMain(iface)
'''
