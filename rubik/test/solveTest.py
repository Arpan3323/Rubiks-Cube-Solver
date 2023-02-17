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
#                test 100: checks the rotations needed when top daisy exists and F,R,B, & L faces
#                          edges are aligned with their centers
#
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


