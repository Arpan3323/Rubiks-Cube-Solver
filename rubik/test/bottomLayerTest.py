'''
Created on Mar 9, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomLayer as bl
import rubik.model.cube as cube


class BottomLayerTest(unittest.TestCase):


    def test100_bottomLayer_checkIfBottomLayerIsSolved(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotation = bl.solveBottomLayer(theCube)
        self.assertEquals(actualRotation, '')
        
    def test101_bottomLayer_createABottomCrossIfItDoesNotExist(self):
        encodedCube = 'orobbggyowyrorwgrywryggrbywbowgoobwyrwgwyogybrbybwbrgo'
        expectedCube = 'gggobgwbbrbbrrgyrgwrbygyrgwybyboygoboyrryooowowrwwwowy'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.alignToBottomCross(theCube))
        self.assertEquals(actualRotatedCube, expectedCube)
        
        
        
