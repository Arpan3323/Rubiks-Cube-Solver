from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):


# Analysis of Rotate:
#        Rotate: a class, receives a dictionary that contains a cube key with values representing the faces of a cube
#          and a dir key with values indicating the direction in which the cube should be rotated.
#        Methods: rotate        receives a dictionary with cube and dir keys and extracts the cube and dir values from
#                               the received dictionary and passes it to the cube class to perform rotations
#        inputs:     
#            Cube        string, 54 characters, must have six unique characters, 5th, 14th, 23rd, 32nd, 41st, and 50th
#                        characters must be unique, mandatory, unvalidate
#
#            dir        string , len .GE. 0, [FfRrBbLlUu], optional, defaults to "F" if missing, D and d are not allowed, 
#                       arrives unvalidated
#        output:
#            normal output:
#                {'cube': 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy', 'status': 'ok'} if everything is okay
#            sad output:
#                {'status': 'error: invalid rotation'} when rotation is invalid (for D and d)
#                {'status': 'error: invalid cube'} when cube is invalid
#                {'status': 'error: extraneous key detected'} if there is additional key in the dictionary
#                {'status': 'error: invalid cube and invalid key'} if both key and cube are invalid
#
#     Happy path tests:
#                test001 = Test that the stubbed rotate returns the correct result
#     Sad path test:
#                test002 = checks if the incoming cube has 54 characters
#                test003 = checks if an error is returned when the incoming direction is D
#                test004 = checks if an error is returned when the incoming direction is d
#                test005 = checks if the cube has 6 unique characters
#                test006 = checks if the cube is None
#                test007 = checks if the cube has nine characters for each of the face
#
#                
                
    def test001_rotate_returnStubbedSolution(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(result.get('cube'), "bbbbbbbbbyrryrryrroooooooooggwggwggwyyyyyygggrrrwwwwww")
        
    
    def test002_rotate_Checking54charactersinCube(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual(result['status'], "error: invalid cube")
        
    def test003_rotate_CheckingIfDirectionToRotateIsD(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'D'
        result = rotate(parms)
        self.assertEqual(result['status'], "error: invalid rotation")
        
    def test004_rotate_CheckingIfDirectionToRotateIsd(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'd'
        result = rotate(parms)
        self.assertEqual(result['status'], "error: invalid rotation")
        
    def test005_rotate_CheckingIfCubeHasSixUniqueCharacters(self):
        encodedCube = 'gggggggggggggggggggggggggggggggggggggggggggggggggggggg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual(result['status'], "error: invalid cube")
        
    def test006_rotate_CheckingIfCubeIsNone(self):
        encodedCube = None
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual(result['status'], "error: invalid cube")
        
    def test007_rotate_CheckingIfCubeHasNineCharactersForEachFace(self):
        encodedCube = 'B00000000BBBBBBBBBbbbbbbbbbrrrrrrrrrooooooooo666666666'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual(result['status'], "error: invalid cube")
