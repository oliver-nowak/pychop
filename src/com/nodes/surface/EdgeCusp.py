'''
Created on Oct 18, 2009

@author: blueAnt
'''

import hou

class EdgeCusp(hou.Node):
    '''
    EdgeCusp surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        EdgeCusp.geoNode = _geoNode
        EdgeCusp.shapeNode = _shapeNode
        EdgeCusp.geo = EdgeCusp.geoNode.createNode('edgecusp')
        
    def group(self, pattern=None):
        return EdgeCusp.geo.parm('group').set(pattern)

    def moveToGoodPosition(self):
        return EdgeCusp.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return EdgeCusp.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return EdgeCusp.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return EdgeCusp.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
        
        