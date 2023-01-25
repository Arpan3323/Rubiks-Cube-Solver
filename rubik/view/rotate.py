from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    directions = parms.get('dir')
    theCube.rotate(directions)
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result