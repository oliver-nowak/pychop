'''
Created on Oct 14, 2009

@author: blueAnt
'''

import hou

class Hole(hou.Node):
    '''
    Hole surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None
    
    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        
        Hole.geoNode = _geoNode
        Hole.shapeNode = _shapeNode
        Hole.geo = Hole.geoNode.createNode('hole')
        
    def __str__(self):
        return "Hole surface node"
        
    def group(self, points=None):
        return Hole.geo.parm('group').set(points)
    
    def breakHoles(self, unbridgeHoles=False):
        return Hole.geo.parm('break').set(unbridgeHoles)
    
    def dist(self, distance=0.000):
        return Hole.geo.parm('distance').set(distance)
    
    def angle(self, holeAngle=0.000):
        return Hole.geo.parm('angle').set(holeAngle)
    
    def snap(self, snapHoles=False):
        return Hole.geo.parm('snap').set(snapHoles)
    
    def moveToGoodPosition(self):
        return Hole.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return Hole.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return Hole.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return Hole.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    