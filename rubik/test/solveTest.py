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
#

    def test100_solve_checkIfAlreadySolved(self):
        parms = {}
        parms['cube'] = 'gggggggggbbbbbbbbbrrrrrrrrroooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertEqual('', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertEqual('', result['integrity'])
        
    def test101_generateToken_checkTheStringToHash(self):
        parms ={}
        parms['cube'] = 'robbbbbbbrrorrrrrryboggggggbgyooooooyygyyygyywwwwwwwww'
        result = solve(parms)
        #solution = 'RUrURUUrRUrURUUrRUrURUUr'
        username = 'azs0239'
        stringToHash = parms['cube'] + result['solution'] + username
        actualString = _generateToken(parms['cube'], result['solution'])
        self.assertEqual(stringToHash, actualString)
                
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
    
        
        
    
        
    
    


