from rubik.model.cube import Cube
from collections import Counter
from rubik.model.constants import *

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    #creating variables for mandatory cube characters and valid directions
    validDirections = "FfRrBbLlUu"
    mandatoryCharsInCube = 54
    numberOfKeys = 2

    #checking the dictionary for extra keys
    keyList = parms.keys()
    if (len(keyList)) > numberOfKeys:
        result['status'] = "error: extraneous key detected"
        return result
    
    encodedCube = parms.get('cube')
    directions = parms.get('dir')
    theCube = Cube(encodedCube)
    
    #checking if the cube cube is empty, None, consists of characters outside [A-Z][a-z][0-9], or 
    #contains exactly 54 characters
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