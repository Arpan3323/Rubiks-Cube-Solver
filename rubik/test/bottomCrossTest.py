'''
Created on Mar 6, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomCross as bc
from rubik.model.cube import Cube

#testing for the failed customer acceptance test case


class bottomCrossTest(unittest.TestCase):


    def test100_rotateToBottomCross(self):
        encodedCube = 'ybrrgbwrwoggrbbgwgobrwrwowyworroybgrogwyyybyybobowggoy'
        theCube = Cube(encodedCube)
        expectedCube = 'bgrggrrgwoygobybbgorworrorobbgboowoygywgybyyybwrwwwrwy'
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = theCube.rotate(rotations)
        self.assertEqual(rotatedCube, expectedCube)