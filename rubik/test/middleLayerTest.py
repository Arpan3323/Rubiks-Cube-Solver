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
#
#    test 101: aligns the incoming cube to bottom layer configuration if it does not exists
#
#    test 102: checks top layer and top face edges, if found, performs U to align edge on side
#              face with appropriate center.
#
#    potential test: checks top layer and top face edges, if found, performs U's to align edge on side
#              face with appropriate center and then performs U or u rotation depending on where 
#              the matching center for top face edge is.
#
#    potential test: checks top layer and top face edges, if found, performs U's to align edge on side
#              face with appropriate center and then performs U or u rotation depending on where 
#              the matching center for top face edge is and finally calls the trigger.
#    
#    Note: make sure to return a tuple containing cube and rotation for test100_middleLayer_checkIfMiddleLayerIsSolved
#          as solveMiddleLayer is going to return a tuple and solve.py will be looking for a tuple 



class middleLayerTest(unittest.TestCase):


    def test100_middleLayer_checkIfMiddleLayerIsSolved(self):
        encodedCube = 'rgyggggggoogooooooorybbbbbbbbyrrrrrrryyyyygybwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotation = ml.solveMiddleLayer(theCube)[1]
        expectedRotations = ''
        self.assertEquals(actualRotation, expectedRotations)
        
    def test101_middleLayer_alignToBottomLayerIfItDoesNotExists(self):
        encodedCube = 'ywgggrwygrrwbowrrbrbobbgwybboorrwyooyybgywgowggybwyroo'
        expectedCube = 'grbbgggggrryyoyoooggbobobbbybrbrrrrroooyygyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualCube = ml._alignToBottomLayer(theCube)
        self.assertEquals(actualCube, expectedCube)
        
    def test102_middleLayer_checkTopLayerForEdgePair_ifAnEdgePairIsFoundAlignSideFaceEdgeWithCenter(self):
        encodedCube = 'rrobgrgggbyggoyooooorobrbbbggbyrorrrygyyybybywwwwwwwww'
        expectedCube = 'bygbgrgggoorgoyoooggbobrbbbrroyrorrryyybygybywwwwwwwww'
        rotations = ml._checkTopLayerForEdgePair(list(encodedCube))[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(rotatedCube, expectedCube)
        