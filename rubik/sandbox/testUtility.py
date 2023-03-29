import re
from rubik.model.constants import *
from rubik.model.cube import Cube
import random
import itertools
import rubik.controller.bottomCross as bc



'''def cubeRotator(cube):
    rotations = ("FfRrBbLlUu")
    rotationList = []
    
    while (cube[DML] != cube[DMM] or cube[DTM] != cube[DMM] or 
           cube[DBM] != cube[DMM] or cube[DMR] != cube[DMM] or 
           cube[FMM] != cube[FBM] or cube[RMM] != cube[RBM] or 
           cube[BMM] != cube[BBM] or cube[LMM] != cube[LBM]):
        
        randomRotation = random.sample(rotations, 1)
        cube = (Cube(cube).rotate(randomRotation))
        rotationList.append(randomRotation)
        
    return (rotationList)

cube = 'ybrrgbwrwoggrbbgwgobrwrwowyworroybgrogwyyybyybobowggoy'
theCube = Cube('5h999hh9IFUIF55559F59hhFFhF59IUFFhFUU9hUU59UI5IhIIIUIU')
result = bc.solveBottomCross(theCube)
#result = Cube(cube2).rotate('uRUfUULuUUUUbuLuuuRRUUUFFURRUUBBULL')
#print(result)


encodedCube = 'ybrrgbwrwoggrbbgwgobrwrwowyworroybgrogwyyybyybobowggoy'
theCube = Cube(encodedCube)
#expectedCube = 'brgggrrgwoywobbbbgobgrroorobgwyooroyygryybgywbwrwwwywy'
rotations = bc.solveBottomCross(theCube)
rotatedCube = Cube(encodedCube).rotate(rotations)
verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
#print(verifyBottomCross)
#self.assertTrue()
#self.assertEqual(rotatedCube, expectedCube)'''

cube = '7BBNgN7NEEEY7EEggYNN7g7YB7NY7NBYYgENBggYB7Eg7YEBBNYEBg'
cube = cube.replace(cube[4], 'g')
cube = cube.replace(cube[13], 'b')
cube = cube.replace(cube[22], 'r')
cube = cube.replace(cube[31], 'o')
cube = cube.replace(cube[40], 'y')
cube = cube.replace(cube[49], 'w')
print(cube)
