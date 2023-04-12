from rubik.model.constants import *
from rubik.model.cube import Cube
import rubik.controller.upFaceCross as ufc

def solveUpSurface(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the up face is solved.
        
        input:  an instance of the cube class with up-face cross solved
        output: the rotations required to solve the up surface  
    '''  
    cubeString = theCube.get()
    if verifyTopSurfaceExists(cubeString):
        return cubeString, ''
    
    if not ufc.verifyTopCrossExists(cubeString):
        cubeString = _alignToTopCross(theCube)
    
    rotations = ''
    if not verifyTopSurfaceExists(cubeString):
        cubeString, rotations = _createTopSurface(cubeString)
    
    return cubeString, rotations

def verifyTopSurfaceExists(cubeString):
    return(
        ufc.verifyTopCrossExists(cubeString) 
        and cubeString[UBL] == cubeString[UMM]
        and cubeString[UBR] == cubeString[UMM]
        and cubeString[UTL] == cubeString[UMM]
        and cubeString[UTR] == cubeString[UMM]
    )

def _alignToTopCross(theCube):
    topCrossRotations = ufc.solveUpCross(theCube)[1]
    return theCube.rotate(topCrossRotations)

def _createTopSurface(cubeString):
    topSurfaceRotations = ''
    if _isOnlyCross(cubeString):
        cubeString, CrossAlignRotations = _alignTopLayer(cubeString)
        cubeString, firstSurfaceRotations = _performSurfaceRotations(cubeString)
        cubeString, fishRotations = solveFish(cubeString)
        topSurfaceRotations = CrossAlignRotations + firstSurfaceRotations + fishRotations
    elif _isFish(cubeString)[0]:
        cubeString, topSurfaceRotations = solveFish(cubeString)
    else:
        cubeString, topLayerRotations = _alignTopLayer(cubeString)
        cubeString, firstSurfaceRotations = _performSurfaceRotations(cubeString)
        cubeString, crossRotations = _createTopSurface(cubeString)
        topSurfaceRotations = topLayerRotations + firstSurfaceRotations + crossRotations
    return cubeString, topSurfaceRotations

def solveFish(cubeString):
    rotationsForFish = ''
    cubeString, fishAlignRotations = _alignFish(cubeString, _isFish(cubeString)[1])
    cubeString, firstSurfaceRotations = _performSurfaceRotations(cubeString)
    rotationsForFish = fishAlignRotations + firstSurfaceRotations
    if not verifyTopSurfaceExists(cubeString):
        cubeString, newFishRotations = _alignFish(cubeString, _isFish(cubeString)[1])
        cubeString, secondSurfacerotations = _performSurfaceRotations(cubeString)
        rotationsForFish += newFishRotations + secondSurfacerotations
    return cubeString, rotationsForFish

def _isOnlyCross(cubeString):
    return(
        ufc.verifyTopCrossExists(cubeString)
        and cubeString[UBL] != cubeString[UMM]
        and cubeString[UBR] != cubeString[UMM]
        and cubeString[UTL] != cubeString[UMM]
        and cubeString[UTR] != cubeString[UMM]
    )

def _alignTopLayer(cubeString):
    rotations = ''
    while cubeString[LTR] != cubeString[UMM]:
        cubeString = Cube(cubeString).rotate('U')
        rotations += 'U'
    return cubeString, rotations
    
def _performSurfaceRotations(cubeString):
    rotations = 'RUrURUUr'
    return Cube(cubeString).rotate(rotations), rotations

def _isFish(cubeString):
    topCorners = [UBL, UBR, UTL, UTR]
    cornerCount = 0
    if ufc.verifyTopCrossExists(cubeString):
        for corner in topCorners:
            if cubeString[corner] == cubeString[UMM]:
                fishHead = corner
                cornerCount += 1
    return (True, fishHead) if cornerCount == 1 else (False, '')

def _alignFish(cubeString, fishHead):
    fishAlignmentRotations = {
        UBR : 'U',
        UTR : 'UU',
        UTL : 'UUU',
        UBL : '',
    }
    if fishHead != UBL:
        cubeString = Cube(cubeString).rotate(fishAlignmentRotations[fishHead])
    return cubeString, fishAlignmentRotations[fishHead]