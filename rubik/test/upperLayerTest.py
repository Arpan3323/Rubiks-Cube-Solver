'''
Created on Apr 17, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.upFaceCross as ufc
import rubik.controller.upFaceSurface as ufs
import rubik.controller.upperLayer as ul
import rubik.model.cube as cube
from rubik.model.constants import *

#Happy Path Tests:
#    test 100: check if top corners are aligned on each face


class upperLayerTest(unittest.TestCase):


    def test100_upperLayer_checkIfCubeHasTopCornersAlignedOnEachFace(self):
        encodedCube = 'gogggggggbbbbbbbbbrgrrrrrrroroooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        checkTopCorners = ul.verifyTopCornersAligned(encodedCube)
        self.assertTrue(checkTopCorners)
    