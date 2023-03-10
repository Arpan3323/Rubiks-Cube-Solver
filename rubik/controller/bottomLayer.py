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
    bottomLayerExists = ((cubeList[FMM] in cubeList[FBL:FBR+1])and (cubeList[RMM] in cubeList[RBL:RBR+1]) and 
                        (cubeList[BMM] in cubeList[BBL:BBR+1]) and (cubeList[LMM] in cubeList[LBL:LBR+1]) and
                        (cubeList[DMM] in cubeList[DTL:DTR+1]) and (cubeList[DMM] in cubeList[DBL:DBR+1]) and
                        (cubeList[DMM] in cubeList[DML]) and (cubeList[DMM] in cubeList[DMR]))
    return bottomLayerExists 
        
    
