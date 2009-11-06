'''
Created on Oct 14, 2009

@author: blueAnt
'''

class PolyExtrude():
    '''
    PolyExtrude surface node
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        
        PolyExtrude.geoNode = _geoNode
        PolyExtrude.shapeNode = _shapeNode
        PolyExtrude.geo = PolyExtrude.geoNode.createNode('polyextrude')
        
    def __str__(self):
        return "PolyExtrude surface node"
        
    def group(self, points=None):
        return PolyExtrude.geo.parm('group').set(points)
   
    def lrst(self, order=None):
        return PolyExtrude.geo.parm('lrst').set(order)
    
    def lxyz(self, order=None):
        return PolyExtrude.geo.parm('lxyz').set(order)
    
    def ltx(self, amount=0.00):
        return PolyExtrude.geo.parm('ltx').set(amount)
    
    def lty(self, amount=0.00):
        return PolyExtrude.geo.parm('lty').set(amount)
    
    def ltz(self, amount=0.00):
        return PolyExtrude.geo.parm('ltz').set(amount)
    
    def lrx(self, amount=0.000):
        return PolyExtrude.geo.parm('lrx').set(amount)
    
    def lry(self, amount=0.000):
        return PolyExtrude.geo.parm('lry').set(amount)
    
    def lrz(self, amount=0.000):
        return PolyExtrude.geo.parm('lrz').set(amount)
    
    def lsx(self, amount=0.00):
        return PolyExtrude.geo.parm('lsx').set(amount)
    
    def lsy(self, amount=0.00):
        return PolyExtrude.geo.parm('lsy').set(amount)
    
    def inset(self, amount=0.00):
        return PolyExtrude.geo.parm('inset').set(amount)
    
    def localsym(self, symmetry=0):
        return PolyExtrude.geo.parm('localsym').set(symmetry)
    
    def keepshared(self, type=0):
        return PolyExtrude.geo.parm('keepshared').set(type)
    
    def divs(self, divisions=2):
        return PolyExtrude.geo.parm('divs').set(divisions)
    
    def delzeroareasides(self, isDeleted=False):
        return PolyExtrude.geo.parm('delzeroareasides').set(isDeleted)
    
    def delsharedsides(self, isDeleted=False):
        return PolyExtrude.geo.parm('delsharedsides').set(isDeleted)
    
    def orientedge(self, isOriented=False):
        return PolyExtrude.geo.parm('orientedge').set(isOriented)
    
    def consolidate(self, type=0):
        return PolyExtrude.geo.parm('consolidate').set(type)
    
    def tolerance(self, amount=0.000):
        return PolyExtrude.geo.parm('tolerance').set(amount)
    
    def moveToGoodPosition(self):
        return PolyExtrude.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return PolyExtrude.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return PolyExtrude.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return PolyExtrude.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    
    def setFirstInput(self, _geoNode):
        return PolyExtrude.geo.setFirstInput(_geoNode)