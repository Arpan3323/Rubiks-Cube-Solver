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
#    
#    test 101: checks the rotations returned when top layer exists
#
#    test 102: align to solved up face surface configuration if it does not already exists
#
#    test 103: find matching corners on the top layer if any exists


class upperLayerTest(unittest.TestCase):


    def test100_upperLayer_checkIfCubeHasTopCornersAlignedOnEachFace(self):
        encodedCube = 'gogggggggbbbbbbbbbrgrrrrrrroroooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        checkTopCorners = ul.verifyTopCornersAligned(encodedCube)
        self.assertTrue(checkTopCorners)
        
    def test101_upperLayer_checkIfUpperLayerIsSolved(self):
        encodedCube = 'gggggggggbbbbbbbbbrrrrrrrrroooooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotation = ul.solveUpperLayer(theCube)[1]
        expectedRotations = ''
        self.assertEquals(actualRotation, expectedRotations)
        
    def test102_upperLayer_alignToTopSurface(self):
        encodedCube = 'rrrogbybwyrgybrobbwgywrororooyrogogggwbwyboybbggywwwyw'
        expectedCube = 'brbggggggrgrbbbbbbooorrrrrrgbgooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualCube = ul._alignToTopSurface(theCube)
        self.assertEquals(expectedCube, actualCube)
        
    def test103_findMatchingTopCorners_checkIfTopLayerHasMatchingCorners(self):
        encodedCube = 'rogggggggbgrbbbbbbororrrrrrgbbooooooyyyyyyyyywwwwwwwww'
        actualReturn = ul._findMatchingTopCorners(encodedCube)
        expectedReturn = (BTL, BTR)
        self.assertEquals(expectedReturn, actualReturn)
        
    def test104_alignTopCorners_alignMatchingCornersWithAppropriateFace(self):
        encodedCube = 'borggggggogbbbbbbbrrorrrrrrgbgooooooyyyyyyyyywwwwwwwww'
        expectedCube = 'gbgggggggborbbbbbbogbrrrrrrrroooooooyyyyyyyyywwwwwwwww'
        rotations = ul._alignTopCorners(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(expectedCube, rotatedCube)
        
    def test105_alignTopCorners_getTopCornerLocationAfterAlignment(self):
        encodedCube = 'gbgggggggbrrbbbbbboobrrrrrrrgoooooooyyyyyyyyywwwwwwwww'
        cornerLocation = ul._alignTopCorners(encodedCube)[2]
        expectedLocation = FTL
        self.assertEquals(expectedLocation, cornerLocation)
        
    def test106__performCornerRotations_performCornerRotationsDependingOnTheLocationOfCornersAfterAlignment(self):
        encodedCube = 'bggggggggobroooooogobbbbbbbrrorrrrrryyyyyyyyywwwwwwwww'
        expectedCube = 'obyggggggboyooooooorybbbbbbrggrrrrrrgybyyyyyrwwwwwwwww'
        alignedCornerLocation = None
        rotations = ul._performCornerRotations(encodedCube, alignedCornerLocation)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(expectedCube, rotatedCube)
        
    