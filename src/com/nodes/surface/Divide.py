'''
Created on Oct 18, 2009

@author: blueAnt
'''

class Divide():
    '''
    Divide surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        Divide.geoNode = _geoNode
        Divide.shapeNode = _shapeNode
        Divide.geo = Divide.geoNode.createNode('divide')
        
    def __str__(self):
        return "Divide surface node"
        
    def group(self, pattern=None):
        return Divide.geo.parm('group').set(pattern)
    
    def smooth(self, isSmoothed=False):
        return Divide.geo.parm('smooth').set(isSmoothed)
    
    def brick(self, isBricked=False):
        return Divide.geo.parm('brick').set(isBricked)
    
    def removesh(self, isRemoved=False):
        return Divide.geo.parm('removesh').set(isRemoved)
    
    def moveToGoodPosition(self):
        return Divide.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return Divide.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return Divide.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return Divide.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    