from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self.cube = encodedCube
        
    def rotate(self, directions):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        
        #rotating the front face of the cube clockwise
        rotatedCubeList[2] = cubeList[0]
        rotatedCubeList[5] = cubeList[1]
        rotatedCubeList[8] = cubeList[2]
        rotatedCubeList[1] = cubeList[3]
        rotatedCubeList[4] = cubeList[4]
        rotatedCubeList[7] = cubeList[5]
        rotatedCubeList[0] = cubeList[6]
        rotatedCubeList[3] = cubeList[7]
        rotatedCubeList[6] = cubeList[8]
        rotatedCubeList[45] = cubeList[9]
        rotatedCubeList[46] = cubeList[12]
        rotatedCubeList[47] = cubeList[15]
        rotatedCubeList[44] = cubeList[29]
        rotatedCubeList[43] = cubeList[32]
        rotatedCubeList[42] = cubeList[35]
        rotatedCubeList[9] = cubeList[42]
        rotatedCubeList[12] = cubeList[43]
        rotatedCubeList[15] = cubeList[44]
        rotatedCubeList[29] = cubeList[45]
        rotatedCubeList[32] = cubeList[46]
        rotatedCubeList[35] = cubeList[47]
        
        
        #coverting the list to a string
        self.cube = "".join(rotatedCubeList)
    
    def get(self):
        return self.cube
        