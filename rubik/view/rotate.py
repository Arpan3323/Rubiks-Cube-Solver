from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    if len(encodedCube) != 54:
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