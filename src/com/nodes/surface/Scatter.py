'''
Created on Oct 18, 2009

@author: blueAnt
'''

import hou

class Scatter(hou.Node):
    '''
    Scatter surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        Scatter.geoNode = _geoNode
        Scatter.shapeNode = _shapeNode
        Scatter.geo = Scatter.geoNode.createNode('scatter')
        
    def __str__(self):
        return "Scatter surface node"
        
    def group(self, pattern=None):
        return Scatter.geo.parm('group').set(pattern)
        
    def keep(self, isKept=False):
        return Scatter.geo.parm('keep').set(isKept)
    
    def npts(self, points=0):
        return Scatter.geo.parm('npts').set(points)
    
    def moveToGoodPosition(self):
        return Scatter.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return Scatter.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return Scatter.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return Scatter.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    
    