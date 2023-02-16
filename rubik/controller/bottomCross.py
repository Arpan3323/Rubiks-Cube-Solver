import rubik.model.constants
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    '''  
    if _verifyBottomCrossExists(theCube):
        return ''
    
    
    
    return 'F'      #TODO:  remove this stubbed value


#method to check if the incoming cube already has a bottom cross
def _verifyBottomCrossExists(cube):
    if cube[48] != cube[49]:
        return False
    if cube[46] != cube[49]:
        return False
    if cube[52] != cube[49]:
        return False
    if cube[50] != cube[49]:
        return False
    if cube[31] != cube[34]:
        return False
    if cube[4] != cube[7]:
        return False
    if cube[13] != cube[16]:
        return False
    if cube[22] != cube[25]:
        return False
    if cube[49] != cube[48]:
        return False
    return True
