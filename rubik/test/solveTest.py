from unittest import TestCase
from rubik.view.solve import solve
from rubik.view.solve import _generateToken
 

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
        fullToken = _generateToken(parms['cube'], result['solution'])[1]
        self.assertEqual('', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertTrue(result['integrity'] in fullToken)
        
    '''The method that is bieng tested has advanced to its next stage
    def test101_generateToken_checkTheStringToHash(self):
        parms ={}
        parms['cube'] = 'robbbbbbbrrorrrrrryboggggggbgyooooooyygyyygyywwwwwwwww'
        result = solve(parms)
        #solution = 'RUrURUUrRUrURUUrRUrURUUr'
        username = 'azs0239'
        stringToHash = parms['cube'] + result['solution'] + username
        actualString = _generateToken(parms['cube'], result['solution'])
        self.assertEqual(stringToHash, actualString)'''
        
    '''The method that is bieng tested has advanced to its next stage
    def test102_generateToken_checkTheGenratedHash(self):
        parms ={}
        parms['cube'] = 'robbbbbbbrrorrrrrryboggggggbgyooooooyygyyygyywwwwwwwww'
        result = solve(parms)
        hashedString = _generateToken(parms['cube'], result['solution'])
        actualHash = 'bbda5da96687bcf13a4905ea1ff07536a73a2bb92ca79b5c3cd36d3d8881717f'
        self.assertEqual(hashedString, actualHash)'''
        
    def test103_generateToken_checkTheLengthOfRandomSubstringChosenFromHash(self):
        parms ={}
        parms['cube'] = 'oryggggggbggooooooooybbbbbbrbyrrrrrrgyyyyybyrwwwwwwwww'
        result = solve(parms)
        substring = _generateToken(parms['cube'], result['solution'])[0]
        substringLength = 8 
        self.assertEqual(len(substring), substringLength)
        
    def test104_solve_checkIntegrity(self):
        parms = {}
        parms['cube'] = 'gowbgybwogwwrobwyyrrrybobyrywybrryrobwbgyoogrwbggwoggo'
        result = solve(parms)
        integrityLength = 8
        self.assertTrue(result['integrity'] != '')
        self.assertEqual(integrityLength, len(result['integrity']))
        
    def test105_solve_FailedCustomerAcceptanceTest_ExceptionThrownForStringConcatenation(self):
        parms = {}
        parms['cube'] = 'S4qwSSx4SxqSw499xxqx4xxq4qxw9q49xw9qS44SwS9S49wwwqq99w'
        result = solve(parms)
        #self.assertEqual('', result['solution'])
        self.assertEqual('ok', result['status'])
        
    def test106_solve_FailedCustomerAcceptanceTest_ExceptionThrownNonIterableNoneTypeObject(self):
        parms = {}
        parms['cube'] = 'yggbgyrggyrrgbobboobbyrrgrrybrooyoobgrygyyboowwwwwwwww'
        result = solve(parms)
        #self.assertEqual('', result['solution'])
        self.assertEqual('ok', result['status'])
    
    def test107_solve_checkRotaionsForTopCornerConfiguration(self):
        parms = {}
        parms['cube'] = 'ogogggggggogbbbbbbbrbrrrrrrrbrooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertEqual('UFFUrLFFlRUFFRRUbFRRfBURR', result['solution'])
        self.assertEqual('ok', result['status'])
        self.assertTrue(result['integrity'] != '')
    
                
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
    
        
        
    
        
    
    


