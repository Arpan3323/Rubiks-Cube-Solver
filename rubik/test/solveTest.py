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
#                test 107: rotations needed when daisy exists but side edges are not aligned
#                test 108: rotations needed when the top daisy has three petals
#
#    sad path tests:
#                catching the invalid directions, d and D, in rotateTest
#                catching invalid cube in rotateTest
#
#
#    evil path test:
#                none
    
    #uncomment later and remove expected cube
    '''def test100_solve_checkIfBottomCrossAlreadyExists(self):
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
        self.assertEqual('', result['integrity'])'''
    
    
    
        
    #will uncomment later
    ''' def test107_solve_rotationsNeededWhenDaisyExistsAndEdgesAreNotAligned(self):
        parms = {}
        parms['cube'] = 'bgbyoyyowyrorbobbwgbwgrbobggoyoggrggwwowywrwroyrrwryyb'
        result = solve(parms)
        self.assertEqual('UUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])'''
        
    #getting the expected cube as well to make sure the cube is bieng rotated correctly    
    def test108_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnRightFace(self):
        parms = {}
        parms['cube'] = 'wbyooyryoorwgbrgwbbbwyrorryoorbgggrygwowywgybboybwgrgw'
        result = solve(parms)
        self.assertEqual('uRUfUUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test109_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnFrontFace(self):
        parms = {}
        parms['cube'] = 'wbgyowwgryobbbgbogogworyybygrbbgrbgorwwwywrorgyyrwyoro'
        result = solve(parms)
        self.assertEqual('uRUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test110_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnBackFace(self):
        parms = {}
        parms['cube'] = 'rygygrrrgrryboborybgowbgoobwoyorgoobbwrwywgbwwywbwgyyg'
        result = solve(parms)
        self.assertEqual('urUUUFFRRBBLL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test111_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnLeftFace(self):
        parms = {}
        parms['cube'] = 'yygybyryrobwbroyrooorbgrbbrwgbwoowoygwgwyworybgggwgbrw'
        result = solve(parms)
        self.assertEqual('UUbUUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
    
    def test112_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnDownFace(self):
        parms = {}
        parms['cube'] = 'ryrybyrooygyorrwrogrrygbybbbbyrobwowwwowywggbgwggwgoob'
        result = solve(parms)
        self.assertEqual('FFUUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test113_solve_rotationsNeededWhenDaisyHasTwoPetals(self):
        parms = {}
        parms['cube'] = 'rybbgowroygobowbyyurwgbrgwrobwyrrboggwgwyybborgwgwoyor'
        result = solve(parms)
        self.assertEqual('uRRUfUUUbuLuUUUFFRRUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test114_solve_rotationsNeededWhenDaisyHasOnePetal(self):
        parms = {}
        parms['cube'] = 'bywgrrwrgoywbgywgoborgowgbygborbwrorywoyyoyrgbgrbwobwy'
        result = solve(parms)
        self.assertEqual('ULuUULUbUUUUUUbUUUFFRRBBLL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test115_solve_rotationsNeededWhenDaisyHasZeroPetal(self):
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
        
    
        
        
    
        
    
    


