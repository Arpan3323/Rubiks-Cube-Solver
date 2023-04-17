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
    
    return 'D'      #TODO:  remove this stubbed value

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

def _findMatchingTopCorners(cubeString):
    topLayerCorners = [(FTL, FTR), (RTL, RTR), (BTL, BTR), (LTL, LTR)]
    for corners in topLayerCorners:
        return corners if cubeString[corners[0]] == cubeString[corners[1]] else False
