'''
Created on Oct 18, 2009

@author: blueAnt
'''

class PolyWire():
    '''
    PolyWire surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        PolyWire.geoNode = _geoNode
        PolyWire.shapeNode = _shapeNode
        PolyWire.geo = PolyWire.geoNode.createNode('polywire')
        
    def __str__(self):
        return "PolyWire surface node"
        
    def group(self, pattern=None):
        return PolyWire.geo.parm('group').set(pattern)
    
    def radius(self, _radius=0.000):
        return PolyWire.geo.parm('radius').set(_radius)
    
    def maxscale(self, scale=0.00):
        return PolyWire.geo.parm('maxscale').set(scale)
    
    def smooth(self, value=0):
        return PolyWire.geo.parm('smooth').set(value)
    
    def div(self, divisions=0):
        return PolyWire.geo.parm('div').set(divisions)
    
    def segs(self, segments=0):
        return PolyWire.geo.parm('segs').set(segments)
    
    def segscale1(self, segmentScale=0.0):
        return PolyWire.geo.parm('segscale1').set(segmentScale)
    
    def segscale2(self, segmentScale=0.0):
        return PolyWire.geo.parm('segscale2').set(segmentScale)
    
    def moveToGoodPosition(self):
        return PolyWire.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return PolyWire.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return PolyWire.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return PolyWire.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    
    
        
        