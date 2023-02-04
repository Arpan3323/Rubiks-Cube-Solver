from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    if len(encodedCube) != 54:
        result['status'] = "error: invalid cube"
        return result
    
    #creating a list that stores 5th, 14th, 23rd, 32nd, 41st, and 50th characters of the cube string
    cubeCharacterList = [encodedCube[4], encodedCube[13], encodedCube[22], encodedCube[31], encodedCube[40], encodedCube[49]]
    
    #checking if all elements in the cubeCharacterList are unique
    if len(set(cubeCharacterList)) != len(cubeCharacterList):
        result['status'] = "error: invalid cube"
        return result
    
    directions = parms.get('dir')
    
    #Checking if the incoming direction is 'D' or 'd'
    if('D' in directions) or ('d' in directions):
        result['status'] = "error: invalid rotation"
        return result
    
    theCube.rotate(directions)
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result