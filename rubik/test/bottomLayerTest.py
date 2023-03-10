'''
Created on Mar 9, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomLayer as bl
import rubik.model.cube as cube


class BottomLayerTest(unittest.TestCase):


    def test100_bottomLayer_checkIfBottomLayerIsSolved(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotation = bl.solveBottomLayer(theCube)
        actualCube = theCube.rotate(actualRotation)
        self.assertEquals(actualCube, encodedCube)
        
