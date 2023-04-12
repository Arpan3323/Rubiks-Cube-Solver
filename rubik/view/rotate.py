from rubik.model.cube import Cube
from collections import Counter
from rubik.model.constants import *

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    validDirections = "FfRrBbLlUu"
    
    if _isExtraKey(parms):
        result['status'] = "error: extraneous key detected"
        return result
    
    encodedCube = parms.get('cube')
    directions = parms.get('dir')
    theCube = Cube(encodedCube)

    if ((theCube.validateCube(encodedCube) == False) 
        or (theCube.validateUniqueCenters(encodedCube) == False)
        or (theCube.validateNineOfEachCubeCharacters(encodedCube) == False)):
            result['status'] = "error: invalid cube"
            if (directions != None) and (not all(char in validDirections for char in directions)):
                result['status'] = "error: invalid cube and invalid rotation"
            return result   
    elif (directions != None) and (not all(char in validDirections for char in directions)):
        result['status'] = "error: invalid rotation"
        return result
    
    theCube = Cube(encodedCube)
    theCube.rotate(directions)
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result

def _isExtraKey(parms):
    numberOfAllowedKeys = 2
    keyList = parms.keys()
    return (len(keyList)) > numberOfAllowedKeys