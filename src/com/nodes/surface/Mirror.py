'''
Created on Oct 14, 2009

@author: blueAnt
'''

import hou

class Mirror(hou.Node):
    '''
    Mirror surface node
    '''

    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
    
        Mirror.geoNode = _geoNode
        Mirror.shapeNode = _shapeNode
        Mirror.geo = Mirror.geoNode.createNode('mirror')
        
    def group(self, points=None):
        return Mirror.geo.parm('group').set(points)
    
    def dist(self, distance=0.0):
        return Mirror.geo.parm('mirror').set(distance)
    
    def keepOriginal(self, isKeepingOriginal=True):
        return Mirror.geo.parm('keepOriginal').set(isKeepingOriginal)
    
    def consolidatetol(self, tolerance=None):
        return Mirror.geo.parm('consolidatetol').set(tolerance)
    
    def moveToGoodPosition(self):
        return Mirror.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return Mirror.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return Mirror.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return Mirror.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    