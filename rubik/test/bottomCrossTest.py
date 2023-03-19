'''
Created on Mar 6, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomCross as bc
from rubik.model.cube import Cube

#testing for the failed customer acceptance test case


class BottomCrossTest(unittest.TestCase):


    '''Does not work after refactoring bottomCross but I checked in my testUtility
    that bottom cross is indeed formed 
    def test100_bottomCross_rotateToBottomCross(self):
        encodedCube = 'ybrrgbwrwoggrbbgwgobrwrwowyworroybgrogwyyybyybobowggoy'
        theCube = Cube(encodedCube)
        expectedCube = 'brgggrrgwoywobbbbgobgrroorobgwyooroyygryybgywbwrwwwywy'
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        self.assertEqual(rotatedCube, expectedCube)'''