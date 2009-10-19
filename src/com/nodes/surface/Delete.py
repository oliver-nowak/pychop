'''
Created on Oct 18, 2009

@author: blueAnt
'''

import hou

class Delete(hou.Node):
    '''
    Delete surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        Delete.geoNode = _geoNode
        Delete.shapeNode = _shapeNode
        Delete.geo = Delete.geoNode.createNode('delete')
        
    def group(self, pattern=None):
        return Delete.geo.parm('group').set(pattern)     

    def negate(self, isNegated=False):
        return Delete.geo.parm('negate').set(isNegated)    
    
    def entity(self, isEntity=False):
        return Delete.geo.parm('entity').set(isEntity)
    
    def affectdegenerate(self, isAffected=False):
        return Delete.geo.parm('affectdegenerate').set(isAffected)
    
    def moveToGoodPosition(self):
        return Delete.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return Delete.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return Delete.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return Delete.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    