from rubik.model.constants import *
from rubik.model.cube import Cube
import rubik.controller.middleLayer as ml

def solveUpCross(theCube: Cube) -> str:
    cubeString = theCube.get()

    if verifyTopCrossExists(cubeString):
        return [cubeString, '']
    
    if ml.verifyMiddleLayerExists(cubeString) == False:
        cubeString = _alignMiddleLayer(theCube)
      
    return 'L'      #TODO:  remove this stubbed value

def verifyTopCrossExists(cubeString):
    return(ml.verifyMiddleLayerExists(cubeString)
           and cubeString[UBM] == cubeString[UMM]
           and cubeString[UMR] == cubeString[UMM]
           and cubeString[UTM] == cubeString[UMM]
           and cubeString[UML] == cubeString[UMM])

def _alignMiddleLayer(theCube):
    middleLayerRotations = ml.solveMiddleLayer(theCube)[1]
    return theCube.rotate(middleLayerRotations)