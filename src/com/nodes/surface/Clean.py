'''
Created on Oct 18, 2009

@author: blueAnt
'''

class Clean():
    '''
    Clean surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        Clean.geoNode = _geoNode
        Clean.shapeNode = _shapeNode
        Clean.geo = Clean.geoNode.createNode('clean')
        
    def __str__(self):
        return "Clean surface node"
        
    def delunusedpts(self, isDeleted=False):
        return Clean.geo.parm('delunusedpts').set(isDeleted)
    
    def deldegengeo(self, isDeleted=False):
        return Clean.geo.parm('deldegengeo').set(isDeleted)
    
    def fusepts(self, isFused=False):
        return Clean.geo.parm('fusepts').set(isFused)
    
    def orientpoly(self, isOriented=False):
        return Clean.geo.parm('orientpoly').set(isOriented)
    
    def moveToGoodPosition(self):
        return Clean.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return Clean.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return Clean.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return Clean.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)