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
    bottomLayerExists = (cubeList[FBL:FBR+1] == cubeList[FMM] and cubeList[RBL:RBR+1] == cubeList[RMM] and 
                         cubeList[BBL:BBR+1] == cubeList[BMM] and cubeList[LBL:LBR+1] == cubeList[LMM] and
                         cubeList[DTL:DTR+1] == cubeList[DMM] and cubeList[DBL:DBR+1] == cubeList[DMM] and
                         cubeList[DMR,DML] == cubeList[DMM])
    return bottomLayerExists 
        
    
