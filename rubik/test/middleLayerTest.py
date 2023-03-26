'''
Created on Mar 25, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomLayer as bl
import rubik.controller.bottomCross as bc
import rubik.controller.middleLayer as ml
import rubik.model.cube as cube
from rubik.model.constants import *
from rubik.view.solve import solve

#Happy path tests:
#    test 100: checks the rotations returned if middle layer is solved
#    test 101: aligns the incoming cube to bottom layer configuration if it does not exists



class middleLayerTest(unittest.TestCase):


    def test100_middleLayer_checkIfMiddleLayerIsSolved(self):
        encodedCube = 'rgyggggggoogooooooorybbbbbbbbyrrrrrrryyyyygybwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotation = ml.solveMiddleLayer(theCube)
        expectedRotations = ''
        self.assertEquals(actualRotation, expectedRotations)
        
    def test100_middleLayer_alignToBottomLayerIfItDoesNotExists(self):
        encodedCube = 'ywgggrwygrrwbowrrbrbobbgwybboorrwyooyybgywgowggybwyroo'
        expectedCube = 'grbbgggggrryyoyoooggbobobbbybrbrrrrroooyygyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualCube = ''.join(ml._alignToBottomLayer(theCube))
        self.assertEquals(actualCube, expectedCube)