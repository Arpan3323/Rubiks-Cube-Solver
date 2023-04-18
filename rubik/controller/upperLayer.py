from rubik.model.constants import *
from rubik.model.cube import Cube
import rubik.controller.upFaceSurface as ufs

def solveUpperLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
    '''  
    cubeString = theCube.get()
    if verifyTopLayerExists(cubeString):
        return cubeString, ''
    
    if not ufs.verifyTopSurfaceExists(cubeString):
        cubeString = _alignToTopSurface(theCube)
    
    rotations = ''
    if not verifyTopCornersAligned(cubeString):
        cubeString, rotations = _orientTopCorners(cubeString)
    
    return cubeString, rotations

def verifyTopCornersAligned(cubeString):
    return(
        ufs.verifyTopSurfaceExists(cubeString)
        and cubeString[FTL] == cubeString[FMM]
        and cubeString[FTR] == cubeString[FMM]
        and cubeString[RTL] == cubeString[RMM]
        and cubeString[RTR] == cubeString[RMM]
        and cubeString[BTL] == cubeString[BMM]
        and cubeString[BTR] == cubeString[BMM]
        and cubeString[LTL] == cubeString[LMM]
        and cubeString[LTR] == cubeString[LMM]
    )

def verifyTopLayerExists(cubeString):
    return(
        verifyTopCornersAligned(cubeString)
        and cubeString[FTM] == cubeString[FMM]
        and cubeString[RTM] == cubeString[RMM]
        and cubeString[BTM] == cubeString[BMM]
        and cubeString[LTM] == cubeString[LMM]
    )

def _alignToTopSurface(theCube):
    topSurfaceRotations = ufs.solveUpSurface(theCube)[1]
    return theCube.rotate(topSurfaceRotations)

def _orientTopLayer(cubeString):
    orientLayerRotations = ''
    if not verifyTopLayerExists(cubeString):
        if not verifyTopCornersAligned(cubeString):
            cubeString, cornerRotations = _orientTopCorners(cubeString)
            orientLayerRotations += cornerRotations
        while not verifyTopLayerExists(cubeString):
            cubeString, edgeRotations = _performTopLayerRotations(cubeString, _findCompletedFace(cubeString))
            orientLayerRotations += edgeRotations
    return cubeString, orientLayerRotations

def _orientTopCorners(cubeString):
    orientCornerRotations = ''
    while not verifyTopCornersAligned(cubeString):
        cubeString, cornerAlignRotations, alignedCornerLocation = _alignTopCorners(cubeString)
        cubeString, cornerRotations = _performCornerRotations(cubeString, alignedCornerLocation)
        cubeString, fishRotations = ufs.solveUpSurface(Cube(cubeString))
        orientCornerRotations += cornerAlignRotations + cornerRotations + fishRotations
    return cubeString, orientCornerRotations


def _findMatchingTopCorners(cubeString):
    topLayerCorners = [(FTL, FTR), (RTL, RTR), (BTL, BTR), (LTL, LTR)]
    for corners in topLayerCorners:
        if cubeString[corners[0]] == cubeString[corners[1]]:
            return corners
        
def _alignTopCorners(cubeString):
    matchingTopCorners = _findMatchingTopCorners(cubeString)
    alignmentRotations = ''
    if matchingTopCorners != None:
        leftCorner = matchingTopCorners[0]
        distanceToCenter = 4
        newCornerLocation = 9
        offsetForFrontCorner = 27
        while(cubeString[leftCorner] != cubeString[leftCorner + distanceToCenter]):
            cubeString = Cube(cubeString).rotate('U')
            alignmentRotations += 'U'
            if leftCorner != 0:
                leftCorner = leftCorner - newCornerLocation
            else:
                leftCorner = leftCorner + offsetForFrontCorner
        return cubeString, alignmentRotations, leftCorner
    else:
        return cubeString, alignmentRotations, None
    
def _performCornerRotations(cubeString, alignedCornerLocation):
    if verifyTopCornersAligned(cubeString):
        return cubeString, ''
    rotationsForCorners = {
        FTL: 'fUBuFUb',
        RTL: 'rULuRUl',
        BTL: 'bUFuBUf',
        LTL: 'lURuLUr',
        None: 'lURuLUr',
    }
    rotations = rotationsForCorners[alignedCornerLocation]
    return Cube(cubeString).rotate(rotations), rotations

def _findCompletedFace(cubeString):
    lastIndex = 1
    faceToReturn = None
    facesToCheck = {
        FMM : all(pieces == cubeString[FMM]  for pieces in (cubeString[FTL:FBR + lastIndex])),
        RMM: all(pieces == cubeString[RMM]  for pieces in (cubeString[RTL:RBR + lastIndex])),
        BMM : all(pieces == cubeString[BMM]  for pieces in (cubeString[BTL:BBR + lastIndex])),
        LMM: all(pieces == cubeString[LMM]  for pieces in (cubeString[LTL:LBR + lastIndex])),
    }
    for solvedFace in facesToCheck:
        if facesToCheck[solvedFace]:
            faceToReturn = solvedFace
            break
    return faceToReturn

def _performTopLayerRotations(cubeString, solvedFace):
    if verifyTopLayerExists(cubeString):
        return cubeString, ''
    rotationsForFaces = {
        FMM: 'BBUlRBBrLUBB',
        RMM: 'LLUfBLLbFULL',
        BMM: 'FFUrLFFlRUFF',
        LMM: 'RRUbFRRfBURR',
        None: 'FFUrLFFlRUFF'
    }
    rotations = rotationsForFaces[solvedFace]
    return Cube(cubeString).rotate(rotations), rotations
            
        