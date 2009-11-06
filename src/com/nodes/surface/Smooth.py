'''
Created on Oct 18, 2009

@author: blueAnt
'''

class Smooth():
    '''
    Smooth surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        Smooth.geoNode = _geoNode
        Smooth.shapeNode = _shapeNode
        Smooth.geo = Smooth.geoNode.createNode('smooth')
        
    def __str__(self):
        return "Smooth surface node"
        
    def group(self, pattern=None):
        return Smooth.geo.parm('group').set(pattern)
    
    def frequency(self, value=0.000):    
        return Smooth.geo.parm('frequency').set(value)
        
    def iterations(self, value=0):
        return Smooth.geo.parm('iterations').set(value)
    
    def moveToGoodPosition(self):
        return Smooth.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return Smooth.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return Smooth.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return Smooth.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    