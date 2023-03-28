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
#    test 103: checks top layer and top face edges, if found, performs U's to align edge on side
#              face with appropriate center and then performs U or u rotation depending on where 
#              the matching center for top face edge is.
#
#    test 104: checks top layer and top face edges, if found, performs U's to align edge on side
#              face with appropriate center and then performs U or u rotation depending on where 
#              the matching center for top face edge is and finally calls the trigger.
#
#    test 105: checks top layer and top face edges, if found, aligns the edge pair and calls bottom layer
#              alogrithm to fix bottom layer.
#
#    test 106: checks all the edge pairs in top layers and aligns them until no edges are left in the top layer
#
#    test 107: checks if component responsible for flipped edge pair in middle layer performs appropriate
#              face trigger if it finds one in middle layer
#
#    test 108: checks if component responsible for flipped edge pair in middle layer performs appropriate
#              face trigger if it finds one in middle layer and fixes bottom layer
#               
#
#    
#


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
        
    '''The component this test was testing has advanced to its next stage
    def test102_middleLayer_checkTopLayerForEdgePair_ifAnEdgePairIsFoundAlignSideFaceEdgeWithCenter(self):
        encodedCube = 'rrobgrgggbyggoyooooorobrbbbggbyrorrrygyyybybywwwwwwwww'
        expectedCube = 'bygbgrgggoorgoyoooggbobrbbbrroyrorrryyybygybywwwwwwwww'
        rotations = ml._checkTopLayerForEdgePair(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(rotatedCube, expectedCube)'''
        
    '''The component this test was testing has advanced to its next stage
    def test103_middleLayer_checkTopLayerForEdgePair_AlignSideFaceEdgeWithCenterAndRotateTopFaceForTrigger(self):
        encodedCube = 'yybogggggyooroboooyybybrbbbrrgbrbrrryggyygroowwwwwwwww'
        expectedCube = 'rrgogggggyybroboooyooybrbbbyybbrbrrrggogyoyyrwwwwwwwww'
        rotations = ml._checkTopLayerForEdgePair(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(rotatedCube, expectedCube)'''
        

    '''The component this test was testing has advanced to its next stage
    def test104_middleLayer_checkTopLayerForEdgePair_AlignSideFaceEdgeWithCenterRotateTopFaceAndTrigger(self):
        encodedCube = 'ybyygygggbgogoroooboggbbbbborgrrbrrryyyyyororwwwwwwwww'
        expectedCube = 'yboygygggbobgogooyrroobbobbwrgrrbrrrbgyyyyroywwwwwwwwg'
        rotations = ml._checkTopLayerForEdgePair(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(rotatedCube, expectedCube)'''
        
    def test105_middleLayer_checkTopLayerForEdgePair_AlignEdgePairPerformTriggerAndFixBottomLayer(self):
        encodedCube = 'rrbbgbgggybyyoyooogyrrbobbbyyygrrrrrboogyoggowwwwwwwww'
        expectedCube = 'bgyggbggggbgyoyoooyybrbobbbybygrrrrrooroyrryowwwwwwwww'
        rotations = ml._checkTopLayerForEdgePair(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(rotatedCube, expectedCube)
        
    def test106_middleLayer_checkTopLayerForEdgePair_AlignEdgePairsUntilNoneAreLeftToAlign(self):
        encodedCube = 'broggbgggyyrooboooggoybobbbboygryrrryryyyrrbgwwwwwwwww'
        expectedCube = 'yogggggggyryoooooogyybbbbbboyrrrrrrrbgobyybyrwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        rotations = ml.solveMiddleLayer(theCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(rotatedCube, expectedCube)
        
    def test107_middleLayer_checkMiddleLayerForFlippedEdgePair_TriggerEdgeInMiddleLayer(self):
        encodedCube = 'orrggoggggoygooooobyybbbbbbggyrrrrrrobryyybyywwwwwwwww'
        expectedCube = 'orggggggyoogyoogoowoybbbbbbbyyrrrrrrryobygbyywwrwwwwww'
        #theCube = cube.Cube(encodedCube)
        rotations = ml._checkMiddleLayerForFlippedEdgePair(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(rotatedCube, expectedCube)
        
    def test108_middleLayer_checkMiddleLayerForFlippedEdgePair_TriggerEdgeInMiddleLayerandFixBottomLayer(self):
        encodedCube = 'oyyggggggbgyoooooogbrbbrbbbgrybrrrrryyoyyyborwwwwwwwww'
        expectedCube = 'obbggggggrrroooooogyobbobbbyryyrrrrrggyyybbyywwwwwwwww'
        #theCube = cube.Cube(encodedCube)
        rotations = ml._checkMiddleLayerForFlippedEdgePair(encodedCube)[1]
        rotatedCube = cube.Cube(encodedCube).rotate(rotations)
        self.assertEquals(rotatedCube, expectedCube)
    
    
        