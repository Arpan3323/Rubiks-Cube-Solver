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
#
#    test 101: create a top cross configuration on the incoming cube if it does not already exists


class upFaceSurfaceTest(unittest.TestCase):


    def test100_solveUpSurface_checkIfUpFaceSurfaceIsSolved(self):
        encodedCube = 'groggggggbogooooooobbbbbbbbrgrrrrrrryyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotation = ufs.solveUpSurface(theCube)[1]
        expectedRotations = ''
        self.assertEquals(actualRotation, expectedRotations)

    def test101_solveUpCross_alignToTopCrossIfItDoesNotAlreadyExist(self):
        encodedCube = 'oorwgroryybbgoygyowywbbybrwoogorbrwbgrrgyoywbywrgwggbw'
        expectedCube = 'ooyggggggggyoooooobrrbbbbbbgbyrrrrrryyryyybyowwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualCube = ufs._alignToTopCross(theCube)
        self.assertEquals(expectedCube, actualCube)
        
    def test102_isOnlyCross_CheckIfCrossExistsOnTopAndNoCornersMatchTopCenter(self):
        encodedCube = 'ybyggggggbogooooooygybbbbbbororrrrrrbyryyygyrwwwwwwwww'
        checkForCross = ufs._isOnlyCross(encodedCube)
        self.assertTrue(checkForCross)