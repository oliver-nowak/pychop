'''
Created on Oct 15, 2009

@author: blueAnt
'''

class Dissolve():
    '''
    Dissolve surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        Dissolve.geoNode = _geoNode
        Dissolve.shapeNode = _shapeNode
        Dissolve.geo = Dissolve.geoNode.createNode('dissolve')
        
    def __str__(self):
        return "Dissolve surface node"
        
    def group(self, pattern=None):
        return Dissolve.geo.parm('group').set(pattern)
    
    def invertsel(self, mode='delete'|'keep'):
        return Dissolve.geo.parm('invertsel').set(mode)
    
    def compnorms(self, isComp=False):
        return Dissolve.geo.parm('compnorms').set(isComp)
    
    def reminlinepts(self, isRem=False):
        return Dissolve.geo.parm('reminlinepts').set(isRem)
    
    def coltol(self, tolerance=0.00):
        return Dissolve.geo.parm('coltol').set(tolerance)
    
    def remunusedpts(self, unusedPoints=False):
        return Dissolve.geo.parm('remunusedpts').set(unusedPoints)
    
    def moveToGoodPosition(self):
        return Dissolve.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return Dissolve.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return Dissolve.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return Dissolve.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    