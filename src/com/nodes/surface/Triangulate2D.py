'''
Created on Oct 18, 2009

@author: blueAnt
'''

import hou

class Triangulate2D(hou.Node):
    '''
    Triangulate2D surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        Triangulate2D.geoNode = _geoNode
        Triangulate2D.shapeNode = _shapeNode
        Triangulate2D.geo = Triangulate2D.geoNode.createNode('triangulate2d')
        
    def __str__(self):
        return "Triangulate2D surface node"
        
    def points(self, pattern=None):
        return Triangulate2D.geo.parm('points').set(pattern)
        
    def refine(self, isRefined=False):
        return Triangulate2D.geo.parm('refine').set(isRefined)
    
    def keepprims(self, isKept=False):
        return Triangulate2D.geo.parm('keepprims').set(isKept)
    
    def moveToGoodPosition(self):
        return Triangulate2D.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return Triangulate2D.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return Triangulate2D.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return Triangulate2D.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    