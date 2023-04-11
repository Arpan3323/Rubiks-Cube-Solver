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
    
    return 'U'      #TODO:  remove this stubbed value

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
        cubeString, fishRotations = _alignFish(cubeString, _isFish(cubeString)[1])
        cubeString, secondSurfacerotations = _performSurfaceRotations(cubeString)
        topSurfaceRotations = CrossAlignRotations + firstSurfaceRotations + fishRotations + secondSurfacerotations
    elif _isFish(cubeString)[0]:
        cubeString, fishRotations = _alignFish(cubeString, _isFish(cubeString)[1])
        cubeString, firstSurfaceRotations = _performSurfaceRotations(cubeString)
        topSurfaceRotations = fishRotations + firstSurfaceRotations
        if not verifyTopSurfaceExists(cubeString):
            cubeString, newFishRotations = _alignFish(cubeString, _isFish(cubeString)[1])
            cubeString, secondSurfacerotations = _performSurfaceRotations(cubeString)
            topSurfaceRotations += newFishRotations + secondSurfacerotations
    return cubeString, topSurfaceRotations

def _isOnlyCross(cubeString):
    return(
        ufc.verifyTopCrossExists(cubeString)
        and cubeString[UBL] != cubeString[UMM]
        and cubeString[UBR] != cubeString[UMM]
        and cubeString[UTL] != cubeString[UMM]
        and cubeString[UTR] != cubeString[UMM]
    )

def _alignTopLayer(cubeString):
    #if _isOnlyCross(cubeString):
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
    #fishRotations = ''
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