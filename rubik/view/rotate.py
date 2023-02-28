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
    if (theCube.validateCube(encodedCube) == False):
            result['status'] = "error: invalid cube"

            #checking if both cube and direction are invalid
            if not all(char in validDirections for char in directions):
                result['status'] = "error: invalid cube and invalid rotation"
                return result
            
            return result
    
    #checking if the cube has six unique center faces
    if (theCube.validateUniqueCenters(encodedCube) == False):
            result['status'] = "error: invalid cube"
        
            #checking if both cube and direction are invalid
            if not all(char in validDirections for char in directions):
                result['status'] = "error: invalid cube and invalid rotation"
                return result
            
            return result
    
    #checking if each character is repeated exactly 9 times
    if theCube.validateNineOfEachCubeCharacters(encodedCube) == False:
        result['status'] = "error: invalid cube"
     
        #checking if both cube and direction are invalid
        if not all(char in validDirections for char in directions):
            result['status'] = "error: invalid cube and invalid rotation"
            return result
            
        return result
    
    
    #checking if the incoming directions are valid, [FfRrBbLlUu]
    if (directions != None) and (not all(char in validDirections for char in directions)):
        result['status'] = "error: invalid rotation"
        return result
    
    theCube = Cube(encodedCube)
    theCube.rotate(directions)
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result