'''
Created on Apr 10, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomLayer as bl
import rubik.controller.bottomCross as bc
import rubik.controller.middleLayer as ml
import rubik.controller.upFaceCross as ufc
import rubik.model.cube as cube
from rubik.model.constants import *
from rubik.view.solve import solve

#Happy Path Tests
# test 100: check rotations returned when up face already has a cross
#
# test 101: align the incoming cube to middleLayer configuration if it does not already exist
#
# test 102: if incoming cube does not have top cross, check if it has neighbor edges that match UMM
#
# test 103: align top face neighbor edges to 9 o'clock and 12 o'clock
#
# test 104: checks that the component responsible for performing top cross rotations(FURurf) is functioning correctly



class upFaceCrossTest(unittest.TestCase):


    def test100_solveUpCross_checkIfUpFaceCrossIsSolved(self):
        encodedCube = 'rgyggggggoogooooooorybbbbbbbbyrrrrrrryyyyygybwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotation = ufc.solveUpCross(theCube)[1]
        expectedRotations = ''
        self.assertEquals(actualRotation, expectedRotations)

    def test101_solveUpCross_alignToMiddleLayer(self):
        encodedCube = 'wyyoggbgrrrbroogyoobgbbywryogbbrwbgrywwyywrogyowwwrobg'
        expectedCube = 'rbrggggggyogoooooooyobbbbbbbyyrrrrrryrygyygybwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualCube = ufc._alignMiddleLayer(theCube)
        self.assertEquals(expectedCube, actualCube)
        
    def test102_createTopCross_checkIfThereAreNeighborEdgesOnTopFaceThatMatchUMM(self):
        encodedCube = 'byyggggggryoooooooygbbbbbbbrrorrrrrryygyybyogwwwwwwwww'
        #theCube = cube.Cube(encodedCube)
        checkForNieghbors = ufc._createTopCross(encodedCube)
        self.assertTrue(checkForNieghbors)

    def test103_alignTopNeighbors_checkIfNeighborEdgesOnTopFaceAreAligned(self):
        encodedCube = 'ryoggggggygboooooorrobbbbbbbyyrrrrrryyyoyygbgwwwwwwwww'
        expectedCube = 'byyggggggryoooooooygbbbbbbbrrorrrrrryygyybyogwwwwwwwww'
        rotationsToAlignNieghbors = ufc._alignTopNeighbors(encodedCube, UMR, UTM)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotationsToAlignNieghbors)
        self.assertEquals(expectedCube, rotatedCube)
        
    def test104_performCrossRotations_PerformTheSpecificRotationsForTopCross(self):
        encodedCube = 'yyyggggggryoooooooyrybbbbbbobrrrrrrrbygyyobggwwwwwwwww'
        expectedCube = 'yorggggggyryooooooogybbbbbbgbgrrrrrroybyyyrybwwwwwwwww'
        rotationsForTopCross = ufc._performCrossRotations(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotationsForTopCross)
        self.assertEquals(expectedCube, rotatedCube)
        
    def test105_checkTopForNeighbors_checksTopForNeighborsAlignsThemAndCreatesACrossIfFound(self):
        encodedCube = 'yryggggggobrooooooyyybbbbbbryorrrrrrggboyygybwwwwwwwww'
        expectedCube = 'yorggggggyryooooooogybbbbbbgbgrrrrrroybyyyrybwwwwwwwww'
        rotations = ufc._checkTopForNeighbors(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(expectedCube, rotatedCube)
        
    def test106_checkTopForAdjacentEdges_checksTopFaceToForAdjacentEdgesAndAlignsThemWithFrontFaceAndDoesCrossRotation(self):
        encodedCube = 'oygggggggyoyoooooogyrbbbbbbyryrrrrrrbboyyybgrwwwwwwwww'
        expectedCube = 'ybgggggggyryoooooooyybbbbbbbyorrrrrrrobgyygyrwwwwwwwww'
        rotations = ufc._checkTopForAdjacentEdges(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(expectedCube, rotatedCube)
        
    def test107_checkTopForAdjacentEdges_checksTopFaceToForAdjacentEdgesIfNotFoundPerfromsCrossRotationAndChecksAgain(self):
        encodedCube = 'oyyggggggbyooooooobygbbbbbbyygrrrrrrrbyoygyrrwwwwwwwww'
        expectedCube = 'gbrggggggyrbooooooyyybbbbbbryyrrrrrrggooyyoybwwwwwwwww'
        rotations = ufc._checkTopForAdjacentEdges(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(expectedCube, rotatedCube)
    
    def test108_checkTopForAdjacentEdges_checksTopFaceToForAdjacentEdgesAlignsAndRotatesThemAndCallsComponentToCheckNeighbors(self):
        encodedCube = 'gyoggggggyrbooooooryybbbbbboorrrrrrrbbyyyyyggwwwwwwwww'
        expectedCube = 'ogrgggggggboooooooyrbbbbbbbroyrrrrrryygyyybyywwwwwwwww'
        rotations = ufc._checkTopForAdjacentEdges(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(expectedCube, rotatedCube)
        
    
