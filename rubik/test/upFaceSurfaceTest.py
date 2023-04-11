'''
Created on Apr 11, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomLayer as bl
import rubik.controller.bottomCross as bc
import rubik.controller.middleLayer as ml
import rubik.controller.upFaceCross as ufc
import rubik.controller.upFaceSurface as ufs
import rubik.model.cube as cube
from rubik.model.constants import *
from rubik.view.solve import solve

#Happy Path Tests:
#    test 100: check rotations returned if up surface is already solved


class upFaceSurfaceTest(unittest.TestCase):


    def test100_solveUpCross_checkIfUpFaceCrossIsSolved(self):
        encodedCube = 'groggggggbogooooooobbbbbbbbrgrrrrrrryyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotation = ufs.solveUpSurface(theCube)[1]
        expectedRotations = ''
        self.assertEquals(actualRotation, expectedRotations)
