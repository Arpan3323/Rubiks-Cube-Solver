from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    
    #checking the dictionary for extra keys
    numberOfAllowedKeys = 1
    keyList = parms.keys()
    if (len(keyList)) > numberOfAllowedKeys:
        result['status'] = "error: extraneous key detected"
        return result
     
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    validateCubeString =  theCube.validateCube(encodedCube)
    validateNineUniqueCubeChar = theCube.validateNineOfEachCubeCharacters(encodedCube)
    
    if validateCubeString == False or validateNineUniqueCubeChar == False:
        result['status'] = 'error: invalid cube'
        return result
    
    rotations = ''
    rotations += solveBottomCross(theCube)      #iteration 2
    #rotations += solveBottomLayer(theCube)      #iteration 3
    #rotations += solveMiddleLayer(theCube)      #iteration 4
    #rotations += solveUpCross(theCube)          #iteration 5
    #rotations += solveUpSurface(theCube)        #iteration 5
    #rotations += solveUpperLayer(theCube)       #iteration 6
    
    result['solution'] = rotations
    #result['rotatedCube'] = rotations[1]
    result['status'] = 'ok'    
    result['integrity'] = ''                    #iteration 3
                     
    return result

#testing = solve('wbyooyryoorwgbrgwbbbwyrorryoorbgggrygwowywgybboybwgrgw')
#print(testing)