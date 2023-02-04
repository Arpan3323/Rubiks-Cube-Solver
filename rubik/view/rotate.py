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
    if (len(keyList)) != numberOfKeys:
        result['status'] = "error: extraneous key detected"
        return result
    
    encodedCube = parms.get('cube')
    directions = parms.get('dir')
    
    #checking if the cube cube is empty, None, consists of characters outside [A-Z][a-z][0-9], or 
    #contains exactly 54 characters
    if (
        (encodedCube == None) or 
        (encodedCube.isalnum() == False) or 
        (len(encodedCube) != mandatoryCharsInCube)
        ):
            result['status'] = "error: invalid cube"
        
            #checking if both cube and direction are invalid
            if not all(char in validDirections for char in directions):
                result['status'] = "error: invalid cube and invalid rotation"
                return result
            
            return result
    
    #creating a list that stores 5th, 14th, 23rd, 32nd, 41st, and 50th characters of the cube string
    cubeCharacterList = [encodedCube[FMM], 
                         encodedCube[RMM], 
                         encodedCube[BMM], 
                         encodedCube[LMM], 
                         encodedCube[UMM], 
                         encodedCube[DMM]]
    
    #creating variables to store the set length and list length of the cubeCharacterList
    cubeSetLength = len(set(cubeCharacterList))
    cubeListLength = len(cubeCharacterList)
    
    #checking if the cube contains exactly 54 characters and has six unique center faces
    if (cubeSetLength != cubeListLength):
            result['status'] = "error: invalid cube"
        
            #checking if both cube and direction are invalid
            if not all(char in validDirections for char in directions):
                result['status'] = "error: invalid cube and invalid rotation"
                return result
            
            return result
    
    #checking if each character is repeated exactly 9 times
    for value in Counter(encodedCube).values():
        if value != 9:
            result['status'] = "error: invalid cube"
            
            #checking if both cube and direction are invalid
            if not all(char in validDirections for char in directions):
                result['status'] = "error: invalid cube and invalid rotation"
                return result
            
            return result
    
    
    #checking if the incoming directions are valid, [FfRrBbLlUu]
    if not all(char in validDirections for char in directions):
        result['status'] = "error: invalid rotation"
        return result
    
    theCube = Cube(encodedCube)
    theCube.rotate(directions)
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result