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
        
    def test103_alignTopLayer_rotatesTopFaceUntilACornerPieceIsInLeftTopRight(self):
        encodedCube = 'ybyggggggbogooooooygybbbbbbororrrrrrbyryyygyrwwwwwwwww'
        expectedCube = 'bogggggggygyooooooorobbbbbbybyrrrrrrgybyyyryrwwwwwwwww'
        rotations = ufs._alignTopLayer(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(expectedCube, rotatedCube)
    
    def test104_performSurfaceRotations_PerformTheSpecificRotationsForSolvingTopSurface(self):
        encodedCube = 'bogggggggygyooooooorobbbbbbybyrrrrrrgybyyyryrwwwwwwwww'
        expectedCube = 'boygggggggbyoooooobgybbbbbbrrorrrrrrgyryyyyyowwwwwwwww'
        rotationsForTopSurface = ufs._performSurfaceRotations(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotationsForTopSurface)
        self.assertEquals(expectedCube, rotatedCube)
        
    def test105_isFish_CheckIfTopSurfaceHasAFish(self):
        encodedCube = 'boygggggggbyoooooobgybbbbbbrrorrrrrrgyryyyyyowwwwwwwww'
        checkForFish = ufs._isFish(encodedCube)
        self.assertTrue(checkForFish)
        
    def test106_alignFish_RotatesTopUntilFishHeadIsOrientedCorrectlyOnUpBottomLeft(self):
        encodedCube = 'gbyggggggbgyoooooorrobbbbbbboyrrrrrryygyyyoyrwwwwwwwww'
        expectedCube = 'boygggggggbyoooooobgybbbbbbrrorrrrrrgyryyyyyowwwwwwwww'
        fishHead = UTL
        rotations = ufs._alignFish(encodedCube, fishHead)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(expectedCube, rotatedCube)
        
    def test107_createTopSurface_IfOnlyCrossExistsAlignsItCreatesFishAndSolvesTopSurface(self):
        encodedCube = 'ybyggggggogbbbbbbbyoyrrrrrrrrroooooooygyyybygwwwwwwwww'
        expectedCube = 'gggggggggbrrbbbbbbobbrrrrrrrooooooooyyyyyyyyywwwwwwwww'
        rotations = ufs._createTopSurface(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(expectedCube, rotatedCube)
        
    def test108_createTopSurface_IfAFishAlreadyExistsCheckIfRotatingOnceWillSolve(self):
        encodedCube = 'ybbbbbbbbyrgrrrrrroorggggggyggoooooobyyyyyryowwwwwwwww'
        expectedCube = 'ggobbbbbbbrgrrrrrrobbggggggrorooooooyyyyyyyyywwwwwwwww'
        rotations = ufs._createTopSurface(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(expectedCube, rotatedCube)
    
    def test109_createTopSurface_WhenTopHasCrossAndMoreThanOneCornerThatMatchTopCenter(self):
        encodedCube = 'rrobbbbbbyborrrrrrbgyggggggroboooooogyyyyyyygwwwwwwwww'
        expectedCube = 'ooobbbbbbbrrrrrrrrgbbggggggrggooooooyyyyyyyyywwwwwwwww'
        rotations = ufs._createTopSurface(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(expectedCube, rotatedCube)
        
        
        