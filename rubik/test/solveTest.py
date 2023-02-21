from unittest import TestCase
from rubik.view.solve import solve
 

class SolveTest(TestCase):
        
#Analysis of Solve
#
#    Solve: receives a dictionary that contains a cube key with values representing the faces of a cube.
#           performs rotations on an unsolved cube to solve it. Currently only solves for bottom cross
#    
#    output:    
#        If the input cube is valid :
#                        {solution':'recorded_rotations', 'status': 'ok', 'integrity':''} 
#                            where value of 'solution’ describes rotations
#                            'status' is 'ok'
#                            'integrity' is ''     
#        If the input cube is invalid or extraneous keys are present:
#                        {‘status’: ‘error: xxx’}
#                            where ‘xxx’ is an error message of the developer’s choosing
#
#
#
#    Analysis: bottomCross.SolveBottomCross
#        inputs:
#            theCube: a string representing the 54 characters of the cube
#        output: 
#            side-effects: no external effects, internal changes only
#            nominal:  returns the rotations performed to achieve bottom face cross orientation
#            abnormal: 
#
#    happy path tests:
#                test 100: checks if solution contains no rotations when the bottom cross exists
#                test 101: checks the rotations needed when top daisy exists and F,R,B, & L faces
#                          edges are aligned with their centers
#                test 102: checks the rotations needed when top daisy exists and F,R,B, & L faces
#                          edges are aligned with their centers and the front face has been rotated once
#                test 103: checks the rotations needed when top daisy exists and F,R,B, & L faces
#                          edges are aligned with their centers and the front face has been rotated twice
#                test 104: checks the rotations needed when top daisy exists and F,R,B, & L faces
#                          edges are aligned with their centers and the front and right face has been rotated twice
#                test 105: checks the rotations needed when top daisy exists and F,R,B, & L faces
#                          edges are aligned with their centers and the front and right face has been rotated twice
#                          and back face has been rotated once
#                test 106: checks the rotations needed when top daisy exists and F,R,B, & L faces
#                          edges are aligned with their centers and the front, right, and back face has been rotated twice
#                          and left face has been rotated once
#                test 107: rotations needed when daisy exists but side edges are not aligned 
#
#    sad path tests:
#                catching the invalid directions, d and D, in rotateTest
#                catching invalid cube in rotateTest
#
#
#    evil path test:
#                none

    def test100_solve_checkIfBottomCrossAlreadyExists(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertEqual('', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
    
    def test101_solve_rotationsNeededWhenDaisyExistsAndEdgesAligned(self):
        parms = {}
        parms['cube'] = 'rbyyborrbbrwgryogyogwbgybygboyrogyowowgwywgwrgbybwroor'
        result = solve(parms)
        self.assertEqual('FFRRBBLL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test102_solve_rotationsNeededWhenDaisyHasBeenRotatedOnceFromFront(self):
        parms = {}
        parms['cube'] = 'ryrrbbboygrwwryrgyogwbgybygbogrobyoyowgwywwgyogbbwroor'
        result = solve(parms)
        self.assertEqual('FRRBBLL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
             
    def test103_solve_rotationsNeededWhenDaisyHasBeenRotatedTwiceFromFront(self):
        parms = {}
        parms['cube'] = 'brrobyybrwrwgryygyogwbgybygboorogyobowgwywybgrwgbwroor'
        result = solve(parms)
        self.assertEqual('RRBBLL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test104_solve_rotationsNeededWhenDaisyHasBeenRotatedTwiceFromFrontAndRight(self):
        parms = {}
        parms['cube'] = 'brbobbyboygyyrgwrwrgwygyrygboorogyobowgwyrybrrwgbwwoog'
        result = solve(parms)
        self.assertEqual('BBLL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test105_solve_rotationsNeededWhenDaisyHasBeenRotatedTwiceFromFrontAndRightAndOnceFromBack(self):
        parms = {}
        parms['cube'] = 'brbobbyboyggyrowroryrygggywgoowogoobygwwyrybrrwgbwwbry'
        result = solve(parms)
        self.assertEqual('BLL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
    
    def test106_solve_rotationsNeededWhenDaisyHasBeenRotatedTwiceFromEverySideAndOnceFromLeft(self):
        parms = {}
        parms['cube'] = 'grbwbbyboygyyrrwrbgygygbwgrygwooobgorooyyrrbrbwgowwywo'
        result = solve(parms)
        self.assertEqual('L', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
    
    def test107_solve_rotationsNeededWhenDaisyExistsAndEdgesAreNotAligned(self):
        parms = {}
        parms['cube'] = 'bgbyoyyowyrorbobbwgbwgrbobggoyoggrggwwowywrwroyrrwryyb'
        result = solve(parms)
        self.assertEqual('UUUFFUURRUUBBUULL' or 'ULLRRUUFFBB', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    


