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

def _isOnlyCross(cubeString):
    return(
        ufc.verifyTopCrossExists(cubeString)
        and cubeString[UBL] != cubeString[UMM]
        and cubeString[UBR] != cubeString[UMM]
        and cubeString[UTL] != cubeString[UMM]
        and cubeString[UTR] != cubeString[UMM]
    )