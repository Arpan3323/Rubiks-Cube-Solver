from rubik.model.constants import *
from rubik.model.cube import Cube
import rubik.controller.bottomLayer as bl

def solveMiddleLayer(theCube: Cube) -> str:

    cubeList = list(theCube.get())

    if verifyMiddleLayerExists(cubeList):
        return ''
    
    if bl.verifyBottomLayerExists(cubeList) == False:
        cubeList = _alignToBottomLayer(theCube)
    
    return 'B'      #TODO:  remove this stubbed value

def verifyMiddleLayerExists(cubeList):
    return(bl.verifyBottomLayerExists(cubeList) 
           and cubeList[FMM] == cubeList[FML]
           and cubeList[FMM] == cubeList[FMR]
           and cubeList[RMM] == cubeList[RML]
           and cubeList[RMM] == cubeList[RMR]
           and cubeList[BMM] == cubeList[BML]
           and cubeList[BMM] == cubeList[BMR]
           and cubeList[LMM] == cubeList[LML]
           and cubeList[LMM] == cubeList[LMR])

def _alignToBottomLayer(theCube):
    bottomLayerCube = bl.solveBottomLayer(theCube)[0]
    return bottomLayerCube
