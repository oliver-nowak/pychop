'''
Created on Oct 1, 2009

@author: Wintermute
'''
import hou

if __name__== '__main__':
    pass

class Group(hou.Node):
    '''
    Group surface node
    
    Generates groups of points or primitives according to various criteria.
    '''
    
    geoNode = None
    shapeNode = None
    geo = None


    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        
        Group.geoNode   = _geoNode
        Group.shapeNode = _shapeNode
        Group.geo = Group.geoNode.createNode('group')
        
    def crname(self, name=None):
        '''
        crname(name)
        
        The name of the group to create.
        '''
        
        return Group.geo.parm('crname').set(name)
        
    def entity(self, type=None):
        '''
        entity(type)
        
        Whether to create a primitive or point group. 
                        
        Parameters: 
            [0] 'primitive' : select primives 
            [1] 'point'     : select points'''
        return Group.geo.parm('entity').set(type)
    
    def geotype(self, type=None):
        '''
        geotype(type)
        
        What sort of primitives to allow in the group.
        
        Parameters:
            [0] 'all'    : select all geometry types '''
        return Group.geo.parm('geotype').set(type)
        
    def groupnumber(self, type=None):
        '''
        groupnumber(boolean)
        
        Enable grouping by number.
        '''
        return Group.geo.parm('groupnumber').set(type)
    
    def ordered(self, isOrdered=False):
        '''
        ordered(boolean)
        
        Orders the points/primitives in the group in the order they are entered. Useful when skinning.
        '''
        return Group.geo.parm('ordered').set(isOrdered)
   
    def filter(self, amount=None):
        '''
        filter(int)
       
        This is evaluated for every point or primitive. If it is true, the element is added to the group. It supports all the local variables of the Point and Primitive operations.
       
        Parameters:
            0 - 100
        '''
        return Group.geo.parm('filter').set(amount)
    
    def pattern(self, _pattern=None):
        '''
        pattern(n)
        
        Enter the pattern to be grouped.
        
        Parameters:
            n
            n - (n+1)
            n n n [space delimited list]
        '''
        return Group.geo.parm('pattern').set(_pattern)
            
        
    def groupop(self, type=None):
        '''
        groupop(type)
        
        Group by a pattern, a range, or an expression.
        
        Parameters:
            [0] 'grppattern    :
            [1] 'grprange      :
            [2] 'grpexpression : '''
        return Group.geo.parm('groupop').set(type)
        
    def moveToGoodPosition(self):
        return Group.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return Group.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return Group.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return Group.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    
        