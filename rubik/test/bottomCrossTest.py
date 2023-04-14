'''
Created on Mar 6, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomCross as bc
from rubik.model.cube import Cube

#    Analysis: bottomCross.SolveBottomCross
#        inputs:
#            theCube: a string representing the 54 characters of the cube
#        output: 
#            side-effects: no external effects, internal changes only
#            nominal:  returns the rotations performed to achieve bottom face cross orientation
#            abnormal: returns a dictionary with a key of status and a value describing the error
#
#    happy path tests:
#                test 100: checks if solution contains no rotations when the bottom cross exists
#                test 101: checks the rotations needed when top daisy exists and F,R,B, & L faces
#                          edges are aligned with their centers
#                test 102: rotations needed when daisy exists but side edges are not aligned
#                test 103: rotations needed when the top daisy has three petals and required edge is on Right face
#                test 104: rotations needed when the top daisy has three petals and required edge is on Front face
#                test 105: rotations needed when the top daisy has three petals and required edge is on back face
#                test 106: rotations needed when the top daisy has three petals and required edge is on left face
#                test 107: rotations needed when the top daisy has three petals and required edge is on down face
#                test 108: rotations needed when the top daisy has two petals 
#                test 109: rotations needed when the top daisy has one petal
#                test 110: rotations needed when the top daisy has zero petals, full bottom cross
#                test 111: testing the failed customer acceptance test
#                
#
#    sad path tests:
#                captured in solve.py
#
#    evil path test:
#                none
    



class BottomCrossTest(unittest.TestCase):
    def test100_solve_checkIfAlreadySolved(self):
        
        encodedCube = 'gggggggggbbbbbbbbbrrrrrrrrroooooooooyyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        rotationsReturned = bc.solveBottomCross(theCube)
        self.assertEqual('', rotationsReturned)
    
    def test101_solve_rotationsNeededWhenDaisyExistsAndEdgesAligned(self):
        
        encodedCube = 'rgrogyobbgoyoogrrybborbybrwwrgbrggyybwrwywwwygowgwboyo'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)
        
    def test102_solve_rotationsNeededWhenDaisyExistsAndEdgesAreNotAligned(self):
        
        encodedCube = 'bgbyoyyowyrorbobbwgbwgrbobggoyoggrggwwowywrwroyrrwryyb'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)
            
    def test103_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnRightFace(self):
        
        encodedCube = 'wbyooyryoorwgbrgwbbbwyrorryoorbgggrygwowywgybboybwgrgw'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)
        
    def test104_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnFrontFace(self):
        
        encodedCube = 'obwygbrwworyrororrrgrgbbwgyyoyyroogwbwgwywboggbbowygyb'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)
        
    def test105_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnBackFace(self):
        
        encodedCube = 'rygygrrrgrryboborybgowbgoobwoyorgoobbwrwywgbwwywbwgyyg'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)
        
    def test106_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnLeftFace(self):
        
        encodedCube = 'yygybyryrobwbroyrooorbgrbbrwgbwoowoygwgwyworybgggwgbrw'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)
    
    def test107_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnDownFace(self):
        
        encodedCube = 'ryrybyrooygyorrwrogrrygbybbbbyrobwowwwowywggbgwggwgoob'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)
        
    def test108_solve_rotationsNeededWhenDaisyHasTwoPetals(self):
        
        encodedCube = 'orobbggyowyrorwgrywryggrbywbowgoobwyrwgwyogybrbybwbrgo'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)
        
    def test109_solve_rotationsNeededWhenDaisyHasOnePetal(self):
        
        encodedCube = 'bywgrrwrgoywbgywgoborgowgbygborbwrorywoyyoyrgbgrbwobwy'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)
        
    def test110_solve_rotationsNeededWhenDaisyHasZeroPetal(self):
        
        encodedCube = 'wororowwggobwgryrgrywborwwbbgbwbgoroobyyyyrbyggoywgybr'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)


    def test111_bottomCross_rotateToBottomCross(self):
        encodedCube = 'ybrrgbwrwoggrbbgwgobrwrwowyworroybgrogwyyybyybobowggoy'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)
        
    def test112_bottomCross_FailedCustomerAcceptanceTest_ExceptionThrownForStringConcatenation(self):
        encodedCube = 'S4qwSSx4SxqSw499xxqx4xxq4qxw9q49xw9qS44SwS9S49wwwqq99w'
        theCube = Cube(encodedCube)
        rotations = bc.solveBottomCross(theCube)
        rotatedCube = Cube(encodedCube).rotate(rotations)
        verifyBottomCross = bc.verifyBottomCrossExists(list(rotatedCube))
        self.assertTrue(verifyBottomCross)
    