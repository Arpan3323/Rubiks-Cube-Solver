'''
Created on Feb 2, 2023

@author: Arpan Srivastava


'''
import unittest
import rubik.model.cube as cube

#Analysis of Cube
#
#    Cube: a class, receives a string that contains a cube key with values representing the faces of a cube
#          and a dir string with values indicating the direction in which the cube should be rotated.
#    Methods: __init__        constructs a cube from a serialized string 
#             get             yields a serialized string of internal representation
#             rotate            performs rotations on the cube depending on the 'dir' key's value
#
#    Analysis: Cube.rotate
#        inputs:
#            dir: string , len .GE. 0, [FfRrBbLlUu], optional, defaults to "F" if missing, arrives unvalidated
#        output: 
#            side-effects: no external effects, internal changes only
#            nominal:  returns a dictionary containing the cube as a string after performing the rotation on it
#            abnormal: raise Direxcepetion (d & D are not accepted)
#
#    happy path tests:
#                test 001: checks cube rotation in F direction
#                test 002: checks cube rotation in f direction
#                test 003: checks cube rotation in R direction
#                test 004: checks cube rotation in R direction (was modified to check a different string on R rotation)
#                test 005: checks cube rotation in B direction
#                test 006: checks cube rotation in b direction
#                test 007: checks cube rotation in L direction
#                test 008: checks cube rotation in l direction
#                test 009: checks cube rotation in U direction
#                test 010: checks cube rotation in u direction
#                test 011: checks for missing direction, dir=None
#                test 012: checks for empty direction, dir=""
#                test 013: checks for multi-string rotation (modified to include R rotation)
#                test 014: checks for rotation when no argument is provided
#
#
#    sad path tests:
#                catching the invalid directions, d and D, in rotateTest
#                catching invalid cube in rotateTest
#
#
#    evil path test:
#                none


class CubeTest(unittest.TestCase):


    def test_rotate_001_RotatesCubeInFDirection(self):
        cubeToRotate = 'ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        self.assertEqual(rotatedCube, 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg')
        
    def  test_rotate_002_RotatesCubeInfDirection(self):
        cubeToRotate = 'ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('f')
        self.assertEqual(rotatedCube, 'ywwobborbgyoyroybowbrggwwrybwogobgobwwbryggorygrywrryg')

    def  test_rotate_003_RotatesCubeInRDirection(self):
        cubeToRotate = 'lle44ee1T41111T1Y4lYeeT4YYeTTYlYYTe11e41l4TTY4ll4eTYll'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('R')
        self.assertEqual(rotatedCube, 'lll44Te1l114Y114T1YYe4T44YeTTYlYYTe11ee1leTTT4lY4eeYll')
        
    
    def  test_rotate_004_RotatesCubeInrDirection(self):
        cubeToRotate = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('r')
        self.assertEqual(rotatedCube, 'ggwggwggwrrrrrrrrrybbybbybbooooooooowwbwwbwwbyygyygyyg')
    

    def  test_rotate_005_RotatesCubeInBDirection(self):
        cubeToRotate = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('B')
        self.assertEqual(rotatedCube, 'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo')

    def  test_rotate_006_RotatesCubeInbDirection(self):
        cubeToRotate = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b')
        self.assertEqual(rotatedCube, 'gggggggggrrwrrwrrwbbbbbbbbbyooyooyooooowwwwwwyyyyyyrrr')
        
    def  test_rotate_007_RotatesCubeInLDirection(self):
        cubeToRotate = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('L')
        self.assertEqual(rotatedCube, 'wggwggwggrrrrrrrrrbbybbybbyooooooooobwwbwwbwwgyygyygyy')
        
    def  test_rotate_008_RotatesCubeInlDirection(self):
        cubeToRotate = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('l')
        self.assertEqual(rotatedCube, 'yggyggyggrrrrrrrrrbbwbbwbbwooooooooogwwgwwgwwbyybyybyy')
        
    def  test_rotate_009_RotatesCubeInUDirection(self):
        cubeToRotate = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('U')
        self.assertEqual(rotatedCube, 'rrrggggggbbbrrrrrrooobbbbbbgggoooooowwwwwwwwwyyyyyyyyy')

    def  test_rotate_010_RotatesCubeInuDirection(self):
        cubeToRotate = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('u')
        self.assertEqual(rotatedCube, 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy')

    def  test_rotate_011_RotatesCubeInFDirection_IfDirectionIsNone(self):
        cubeToRotate = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate(None)
        self.assertEqual(rotatedCube, 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
        
    def  test_rotate_012_RotatesCubeInFDirection_IfDirectionIsEmpty(self):
        cubeToRotate = 'bboggryowwgogrrrggbrryboobbgrrbowyogybywwowyboygwyyrww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate("")
        self.assertEqual(rotatedCube, 'ygbogbwrowgoyrrbggbrryboobbgroboyyogybywwogwrrgwwyyrww')

    def  test_rotate_013_RotatesCubeInMultipleDirection(self):
        cubeToRotate = 'bboggryowwgogrrrggbrryboobbgrrbowyogybywwowyboygwyyrww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate("FBfUbR")
        self.assertEqual(rotatedCube, 'wggggyyobrgogryowwgrrrbobbbgbobowyogybwywrbowoyywyrrwr')
        
    def  test_rotate_014_RotatesCubeInFDirection_IfDirectionIsMissing(self):
        cubeToRotate = 'bboggryowwgogrrrggbrryboobbgrrbowyogybywwowyboygwyyrww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate()
        self.assertEqual(rotatedCube, 'ygbogbwrowgoyrrbggbrryboobbgroboyyogybywwogwrrgwwyyrww')










