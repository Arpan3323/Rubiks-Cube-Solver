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
#                
#
#    sad path tests:
#                test 901: checking if the cube has 54 characters
#                test 902: checking if the incoming dictionary has extraneous keys
#                test 903: checking if the cube has 9 unique characters
#                test 904: checking if the cube has unique centers
#
#    evil path test:
#                none
    
    #uncomment later and remove expected cube
    def test100_solve_checkIfBottomCrossAlreadyExists(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertEqual('', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
    
    def test101_solve_rotationsNeededWhenDaisyExistsAndEdgesAligned(self):
        parms = {}
        parms['cube'] = 'rgrogyobbgoyoogrrybborbybrwwrgbrggyybwrwywwwygowgwboyo'
        result = solve(parms)
        self.assertEqual('FFRRBBLL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
    
    
    
        
    def test102_solve_rotationsNeededWhenDaisyExistsAndEdgesAreNotAligned(self):
        parms = {}
        parms['cube'] = 'bgbyoyyowyrorbobbwgbwgrbobggoyoggrggwwowywrwroyrrwryyb'
        result = solve(parms)
        self.assertEqual('UUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
            
    def test103_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnRightFace(self):
        parms = {}
        parms['cube'] = 'wrwboworrbrybbbgrrrgryrowgyyogygoogbbwgwywogoybwowygyb'
        result = solve(parms)
        self.assertEqual('uRUfUUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test104_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnFrontFace(self):
        parms = {}
        parms['cube'] = 'wbgyowwgryobbbgbogogworyybygrbbgrbgorwwwywrorgyyrwyoro'
        result = solve(parms)
        self.assertEqual('uRUfUUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test105_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnBackFace(self):
        parms = {}
        parms['cube'] = 'rygygrrrgrryboborybgowbgoobwoyorgoobbwrwywgbwwywbwgyyg'
        result = solve(parms)
        self.assertEqual('urUUUFFRRBBLL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test106_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnLeftFace(self):
        parms = {}
        parms['cube'] = 'yygybyryrobwbroyrooorbgrbbrwgbwoowoygwgwyworybgggwgbrw'
        result = solve(parms)
        self.assertEqual('UUbUUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
    
    def test107_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnDownFace(self):
        parms = {}
        parms['cube'] = 'ryrybyrooygyorrwrogrrygbybbbbyrobwowwwowywggbgwggwgoob'
        result = solve(parms)
        self.assertEqual('FFUUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test108_solve_rotationsNeededWhenDaisyHasTwoPetals(self):
        parms = {}
        parms['cube'] = 'orobbggyowyrorwgrywryggrbywbowgoobwyrwgwyogybrbybwbrgo'
        result = solve(parms)
        self.assertEqual('uRRUfUULUbUUFFRRUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test109_solve_rotationsNeededWhenDaisyHasOnePetal(self):
        parms = {}
        parms['cube'] = 'bywgrrwrgoywbgywgoborgowgbygborbwrorywoyyoyrgbgrbwobwy'
        result = solve(parms)
        self.assertEqual('ULuUULUbUUUUUUbUUUFFRRBBLL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test110_solve_rotationsNeededWhenDaisyHasZeroPetal(self):
        parms = {}
        parms['cube'] = 'wororowwggobwgryrgrywborwwbbgbwbgoroobyyyyrbyggoywgybr'
        result = solve(parms)
        self.assertEqual('fuRUUurUUUUUbuLuuUluFFURRBBULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test901_solve_invalidCube(self):
        parms = {}
        parms['cube'] = 'wororowwgg'
        result = solve(parms)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test902_solve_ExtraneousKeyForSolveServer(self):
        parms = {}
        parms['cube'] = 'wororowwggobwgryrgrywborwwbbgbwbgoroobyyyyrbyggoywgybr'
        parms['extraKey'] = 'FfRfUu'
        result = solve(parms)
        self.assertEqual('error: extraneous key detected', result['status'])
        
    def test903_solve_checkingIfCubeHasNineOfEachCharacter(self):
        parms = {}
        parms['cube'] = 'rbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test904_solve_checkingIfCubeHasSixUniqueCenters(self):
        parms = {}
        parms['cube'] = 'bbbbwbbbbrrrrwrrrroooowooooggggwggggyyyyyyyyybrogwwwww'
        result = solve(parms)
        self.assertEqual('error: invalid cube', result['status'])
    
        
        
    
        
    
    


