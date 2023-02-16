import rubik.model.constants
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cubeList into the down-face cross configuration.
        
        input:  an instance of the cubeList class
        output: the rotations required to transform the input cubeList into the down-face cross 
    '''  
    if _verifyBottomCrossExists(theCube):
        return ''
    
    
    
    return 'F'      #TODO:  remove this stubbed value


#method to check if the incoming cubeList already has a bottom cross
def _verifyBottomCrossExists(cube):
    cube = cube.get()
    cubeList = list(cube)
    if cubeList[48] != cubeList[49]:
        return False
    if cubeList[46] != cubeList[49]:
        return False
    if cubeList[52] != cubeList[49]:
        return False
    if cubeList[50] != cubeList[49]:
        return False
    if cubeList[31] != cubeList[34]:
        return False
    if cubeList[4] != cubeList[7]:
        return False
    if cubeList[13] != cubeList[16]:
        return False
    if cubeList[22] != cubeList[25]:
        return False
    if cubeList[49] != cubeList[48]:
        return False
    return True
