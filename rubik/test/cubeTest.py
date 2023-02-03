'''
Created on Feb 2, 2023

@author: Arpan Srivastava


'''
import unittest
import rubik.model.cube as cube

#Analysis of Cube
#
#    Cube: a class, receives a dictionary that contains a cube key with values representing the faces of a cube
#          and a dir key with values indicating the direction in which the cube should be rotated.
#    Methods: __init__        constructs a cube from a serialized string 
#             get             yields a serialized string of internal representation
#             rotate            performs rotations on the cube depending on the 'dir' key's value
#
#    Analysis: Cube.rotate
#        inputs:
#            dir: string , len .GE. 0, [FfRrBbLlUu], optional, defaults to "F" if missing, arrives unvalidated
#        output: 
#            side-effects: no external effects, internal changes only
#            nominal:  returns a dictionary containing the cube as a string after performing the rotation on it
#            abnormal: raise Direxcepetion (d & D are not accepted)
#
#    happy path tests:
#
#
#    sad path tests:
#
#
#    evil path test:
#                none


class CubeTest(unittest.TestCase):


    def test_rotate_001_RotatesCubeInFDirection(self):
        cubeToRotate = 'ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        self.assertEqual(rotatedCube, 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg')



















