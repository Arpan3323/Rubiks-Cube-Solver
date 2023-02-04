from rubik.model.cube import Cube
from collections import Counter

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    validDirections = "FfRrBbLlUu"

    #checking the dictionary for extra keys
    keyList = parms.keys()
    if (len(keyList)) != 2:
        result['status'] = "error: extraneous key detected"
        return result
    
    encodedCube = parms.get('cube')
    directions = parms.get('dir')
    
    #checking if the cube is none
    if (encodedCube == None) or (encodedCube.isalnum() == False):
        result['status'] = "error: invalid cube"
        
        #checking if both cube and direction are invalid
        if not all(char in validDirections for char in directions):
            result['status'] = "error: invalid cube and invalid rotation"
            return result
        return result
    
    #Checking if each character is repeated exactly 9 times
    for value in Counter(encodedCube).values():
        if value != 9:
            result['status'] = "error: invalid cube"
            
            #checking if both cube and direction are invalid
            if not all(char in validDirections for char in directions):
                result['status'] = "error: invalid cube and invalid rotation"
                return result
            
            return result
            
    
    #creating a list that stores 5th, 14th, 23rd, 32nd, 41st, and 50th characters of the cube string
    cubeCharacterList = [encodedCube[4], encodedCube[13], encodedCube[22], encodedCube[31], encodedCube[40], encodedCube[49]]
    
    #checking if the cube has exactly 54 characters with 6 unique characters and the cube is not equal to none
    if (len(encodedCube) != 54) or (len(set(cubeCharacterList)) != len(cubeCharacterList)):
        result['status'] = "error: invalid cube"
        
        #checking if both cube and direction are invalid
        if not all(char in validDirections for char in directions):
            result['status'] = "error: invalid cube and invalid rotation"
            return result
        
        return result
    
    theCube = Cube(encodedCube)
    
    #Checking if the incoming direction is 'D' or 'd'
    if('D' in directions) or ('d' in directions):
        result['status'] = "error: invalid rotation"
        return result
    
    #checking if the incoming directions are valid, [FfRrBbLlUu]
    if not all(char in validDirections for char in directions):
        result['status'] = "error: invalid rotation"
        return result
        
    theCube.rotate(directions)
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result