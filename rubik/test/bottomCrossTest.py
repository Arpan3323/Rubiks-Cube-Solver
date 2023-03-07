'''
Created on Mar 6, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomCross as bc

#testing for the failed customer acceptance test case


class bottomCrossTest(unittest.TestCase):


    def test100_rotateToBottomCross(self):
        encodedCube = 'ybrrgbwrwoggrbbgwgobrwrwowyworroybgrogwyyybyybobowggoy'
        expectedCube = 'bgrggrrgwoygobybbgorworrorobbgboowoygywgybyyybwrwwwrwy'
        rotations = bc.solveBottomCross(encodedCube)
        rotatedCube = bc.Cube(encodedCube).rotate(rotations)
        self.assertEqual(rotatedCube, expectedCube)