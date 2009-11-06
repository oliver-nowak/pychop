'''
Created on Oct 18, 2009

@author: blueAnt
'''

import hou

class Facet(hou.Node):
    '''
    Facet surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        Facet.geoNode = _geoNode
        Facet.shapeNode = _shapeNode
        Facet.geo = Facet.geoNode.createNode('facet')
        
    def __str__(self):
        return "Facet surface node"
        
    def group(self, pattern=None):
        return Facet.geo.parm('group').set(pattern)
    
    def prenml(self, preCompute=False):
        return Facet.geo.parm('prenml').set(preCompute)
    
    def unique(self, isUnique=False):
        return Facet.geo.parm('unique').set(isUnique)
    
    def cons(self, type=0):
        return Facet.geo.parm('cons').set(type)
    
    def inline(self, isInline=False):
        return Facet.geo.parm('inline').set(isInline)
    
    def orientPolys(self, isOriented=False):
        return Facet.geo.parm('orientPolys').set(isOriented)
    
    def remove(self, isRemoved=False):
        return Facet.geo.parm('remove').set(isRemoved)
    
    def postnml(self, postCompute=False):
        return Facet.geo.parm('postnml').set(postCompute)
    
    def moveToGoodPosition(self):
        return Facet.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return Facet.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return Facet.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return Facet.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    