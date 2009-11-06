'''
Created on Oct 14, 2009

@author: blueAnt
'''

class EdgeCollapse():
    '''
    Edge Collapse surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        EdgeCollapse.geoNode = _geoNode
        EdgeCollapse.shapeNode = _shapeNode
        EdgeCollapse.geo = EdgeCollapse.geoNode.createNode('edgecollapse')
        print 'test ' + str(len(EdgeCollapse.shapeNode.geometry().prims()))

    def __str__(self):
        return "Edge Collapse surface node"
    
    def group(self, pattern=None):
        return EdgeCollapse.geo.parm('group').set(pattern)
     
    def removedegen(self, isRemoved=False):  
        return EdgeCollapse.geo.parm('removedegen').set(isRemoved)
    
    def updatenmls(self, isUpdated=False):
        return EdgeCollapse.geo.parm('updatenmls').set(isUpdated)
    
    def moveToGoodPosition(self):
        return EdgeCollapse.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return EdgeCollapse.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return EdgeCollapse.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return EdgeCollapse.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    