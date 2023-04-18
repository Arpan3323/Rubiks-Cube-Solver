from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
import hashlib
import random

def solve(parms):
    result = {}
    if _isExtraKey(parms):
        result['status'] = "error: extraneous key detected"
        return result
  
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    validateCubeString =  theCube.validateCube(encodedCube)
    validateNineUniqueCubeChar = theCube.validateNineOfEachCubeCharacters(encodedCube) 
    
    if((validateCubeString == False) or 
      (validateNineUniqueCubeChar == False) or 
      (theCube.validateUniqueCenters(encodedCube) == False)):
        result['status'] = 'error: invalid cube'
        return result
    
    rotations = ''
    rotations += solveBottomCross(theCube)      #iteration 2
    rotations += solveBottomLayer(theCube)[1]   #iteration 3
    rotations += solveMiddleLayer(theCube)[1]     #iteration 4
    rotations += solveUpCross(theCube)[1]          #iteration 5
    rotations += solveUpSurface(theCube)[1]        #iteration 5
    rotations += solveUpperLayer(theCube)       #iteration 6
    
    result['solution'] = rotations
    result['status'] = 'ok'    
    result['integrity'] = _generateToken(encodedCube, result['solution'])
    return result

def _generateToken(encodedCube, solution):
    username = 'azs0239'
    stringToHash = encodedCube + solution + username
    sha256Hash = hashlib.sha256()
    sha256Hash.update(stringToHash.encode())
    fullToken = sha256Hash.hexdigest()
    startIndex = random.randint(0, len(fullToken) - 8)
    subToken = fullToken[startIndex:startIndex + 8]
    return subToken

def _isExtraKey(parms):
    numberOfAllowedKeys = 1
    keyList = parms.keys()
    return (len(keyList)) > numberOfAllowedKeys

def _cubeAfterEachIncrement(encodedCube, rotations):
    if rotations == '':
        return Cube(encodedCube)
    rotatedCube = Cube(encodedCube).rotate(rotations)
    return Cube(rotatedCube)