from rubik.model.constants import *
from rubik.model.cube import Cube
import rubik.controller.bottomCross as bc

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''  
    cubeList = list(theCube.get())
    
    if _verifyBottomLayerExists(cubeList):
        return ''
    
    return 'R'      #TODO:  remove this stubbed value

def _verifyBottomLayerExists(cubeList):
    bottomLayerExists = ((cubeList[FBL:FBR+1] in [cubeList[FMM]][0]) and 
                         (cubeList[RBL:RBR+1] in [cubeList[RMM]][0]) and 
                         (cubeList[BBL:BBR+1] in [cubeList[BMM]][0]) and 
                         (cubeList[LBL:LBR+1] in [cubeList[LMM]][0]) and
                         (cubeList[DTL:DTR+1] in [cubeList[DMM]][0]) and 
                         (cubeList[DBL:DBR+1] in [cubeList[DMM]][0]) and
                         (cubeList[DMR,DML] in [cubeList[DMM]][0]))
    return bottomLayerExists 
        
    
