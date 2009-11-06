'''
Created on Oct 18, 2009

@author: blueAnt
'''

class PolyReduce():
    '''
    PolyReduce surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        PolyReduce.geoNode = _geoNode
        PolyReduce.shapeNode = _shapeNode
        PolyReduce.geo = PolyReduce.geoNode.createNode('polyreduce')
        
    def __str__(self):
        return "PolyReduce surface node"
        
    def percentage(self, percent=0):
        return PolyReduce.geo.parm('percentage').set(percent)
        
    def keepedges(self, isKept=False):
        return PolyReduce.geo.parm('keepedges').set(isKept)
    
    def moveToGoodPosition(self):
        return PolyReduce.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return PolyReduce.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return PolyReduce.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return PolyReduce.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    
    def setFirstInput(self, _geoNode):
        return PolyReduce.geo.setFirstInput(_geoNode)