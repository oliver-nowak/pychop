'''
Created on Oct 18, 2009

@author: blueAnt
'''

import hou

class SoftPeak(hou.Node):
    '''
    SoftPeak surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        SoftPeak.geoNode = _geoNode
        SoftPeak.shapeNode = _shapeNode
        SoftPeak.geo = SoftPeak.geoNode.createNode('softpeak')
        
    def group(self, pattern=None):
        return SoftPeak.geo.parm('group').set(pattern)
        
    def dist(self, distance=0.00):
        return SoftPeak.geo.parm('dist').set(distance)
    
    def rad(self, radius=0.000):
        return SoftPeak.geo.parm('rad').set(radius)
    
    def type(self, _type=0):
        return SoftPeak.geo.parm('type').set(_type)
    
    def begintandeg(self, begin=0.000):
        return SoftPeak.geo.parm('begintandeg').set(begin)
    
    def endtandeg(self, end=0.000):
        return SoftPeak.geo.parm('endtandeg').set(end)
    
    def kernel(self, type=0):
        return SoftPeak.geo.parm('kernel').set(type)
    
    def moveToGoodPosition(self):
        return SoftPeak.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return SoftPeak.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return SoftPeak.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return SoftPeak.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    