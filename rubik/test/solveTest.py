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
    
    
    #commented these tests because I had a wrong understanding about the product functionality 
    '''def test102_solve_rotationsNeededWhenDaisyHasBeenRotatedOnceFromFront(self):
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
        expectedCube = 'rrwgoygorbrwbbbbbyoororybrywrwogyggogggbyybgoywywwwrwo'
        result = solve(parms)
        self.assertEqual('uRUfUUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual(expectedCube, result['rotatedCube'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test109_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnFrontFace(self):
        parms = {}
        parms['cube'] = 'wbgyowwgryobbbgbogogworyybygrbbgrbgorwwwywrorgyyrwyoro'
        expectedCube = 'gbyyoowoobgwbbbgbgrgbyryrryogwogrbgowybryorrrgwywwwowy'
        result = solve(parms)
        self.assertEqual('uRUUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual(expectedCube, result['rotatedCube'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    '''def test110_solve_rotationsNeededWhenDaisyHasThreePetalsAndRequiredEdgeisOnBackFace(self):
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
        
    def test113_solve_rotationsNeededWhenDaisyIsMissingOnlyOneEdgeOnAnySide(self):
        parms = {}
        parms['cube'] = 'bbyybyrooryrorrwroygyygbybbgrrrobwowowbwygwwggwggwgoob'
        result = solve(parms)
        self.assertEqual('FFUUUFFUURRUUBBUULL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test113_solve_rotationsNeededWhenDaisyHasTwoPetals(self):
        parms = {}
        parms['cube'] = 'rybbgowroygobowbyyurwgbrgwrobwyrrboggwgwyybborgwgwoyor'
        result = solve(parms)
        self.assertEqual('FFuRuFUUUFFRRBBLL', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])'''
        

        
        
    
        
    
    


