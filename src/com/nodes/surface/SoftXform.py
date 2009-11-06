'''
Created on Oct 14, 2009

@author: blueAnt
'''

if __name__ == '__main__':
    pass


class SoftXform():
    '''
    Soft Transform
    
    Moves the selected point, with smooth rolloff to surrounding points.
    '''
    
    geoNode = None
    shapeNode = None
    geo = None

    def __init__(self, _geoNode, _shapeNode):
        '''
        Constructor
        
        takes a '/geo' Node & shape node
        '''
        
        SoftXform.geoNode = _geoNode
        SoftXform.shapeNode = _shapeNode
        SoftXform.geo = SoftXform.geoNode.createNode('softxform')
        
    def __str__(self):
        return "SoftXform surface node"
        
    def group(self, points=None):
        return SoftXform.geo.parm('group').set(points)
    
    def xOrd(self, order=0):
        return SoftXform.geo.parm('xOrd').set(order)
    
    def rOrd(self, order=0):
        return SoftXform.geo.parm('rOrd').set(order)
    
    def tx(self, amount=0.00):
        return SoftXform.geo.parm('tx').set(amount)
    
    def ty(self, amount=0.00):
        return SoftXform.geo.parm('ty').set(amount)
    
    def tz(self, amount=0.00):
        return SoftXform.geo.parm('tz').set(amount)
    
    def rx(self, amount=0.00):
        return SoftXform.geo.parm('rx').set(amount)
    
    def ry(self, amount=0.00):
        return SoftXform.geo.parm('ry').set(amount)
    
    def rz(self, amount=0.00):
        return SoftXform.geo.parm('rz').set(amount)
        
    def sx(self, amount=1.00):
        return SoftXform.geo.parm('sx').set(amount)
    
    def sy(self, amount=1.00):
        return SoftXform.geo.parm('sy').set(amount)
    
    def sz(self, amount=1.00):
        return SoftXform.geo.parm('sz').set(amount)
    
    def px(self, amount=0.00):
        return SoftXform.geo.parm('px').set(amount)
    
    def py(self, amount=0.00):
        return SoftXform.geo.parm('py').set(amount)
    
    def pz(self, amount=0.00):
        return SoftXform.geo.parm('pz').set(amount)
    
    def shear1(self, amount=0.00):
        return SoftXform.geo.parm('shear1').set(amount)
    
    def shear2(self, amount=0.00):
        return SoftXform.geo.parm('shear2').set(amount)
    
    def shear3(self, amount=0.00):
        return SoftXform.geo.parm('shear3').set(amount)
    
    def rad(self, amount=0.500):
        return SoftXform.geo.parm('rad').set(amount)
    
    def type(self, type=2):
        return SoftXform.geo.parm('type').set(type)
    
    def begintandeg(self, degrees=0.000):
        return SoftXform.geo.parm('begintandeg').set(degrees)
    
    def endtandeg(self, degrees=0.000):
        return SoftXform.geo.parm('endtandeg').set(degrees)
    
    def kernel(self, type=0):
        return SoftXform.geo.parm('kernel').set(type)
    
    def updatenmls(self, isUpdated=True):
        return SoftXform.geo.parm('updatenmls').set(isUpdated)
    
    def moveToGoodPosition(self):
        return SoftXform.geo.moveToGoodPosition()
    
    def setDisplayFlag(self, isDisplayed=False):
        return SoftXform.geo.setDisplayFlag(isDisplayed)
    
    def bypass(self, isBypassed=False):
        return SoftXform.geo.bypass(isBypassed) 
    
    def setCurrent(self, isCurrent=False, clearSelected=False):
        return SoftXform.geo.setCurrent(isCurrent, clear_all_selected=clearSelected)
    