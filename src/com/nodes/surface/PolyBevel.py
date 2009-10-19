'''
Created on Oct 14, 2009

@author: blueAnt
'''

import hou

if __name__== '__main__':
    pass

class PolyBevel(hou.Node):
    '''
    Poly Bevel surface node
    
    Bevels points and edges.
    '''
    
    geoNode = None
    shapeNode = None
    geo = None


    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''

        PolyBevel.geoNode = _geoNode
        PolyBevel.shapeNode = _shapeNode
        PolyBevel.geo = PolyBevel.geoNode.createNode('polybevel')
        
    def group(self, points=None):
        '''
        group(int)
        
        The edges or points to bevel.
        
        Parameters:
        n - (n+1)
        '''
        
        return PolyBevel.geo.parm('group').set(points)
    
    def beveltype(self, type=None):
        '''
        beveltype(int)
        
        The type of beveling to do in your polygon.
        
        Parameters:
        0 : 'flat'
        1 : 
        '''
        
        return PolyBevel.geo.parm('beveltype').set(type)
    
    def relinset(self, value=0.000):
        return PolyBevel.geo.parm('relinset').set(value)
    
    def repetitions(self, reps=0):
        return PolyBevel.geo.parm('repetitions').set(reps)
    
    def updatenmls(self, update=False):
        return PolyBevel.geo.parm('updatenmls').set(update)
    
    def moveToGoodPosition(self):
        return PolyBevel.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return PolyBevel.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return PolyBevel.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return PolyBevel.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    