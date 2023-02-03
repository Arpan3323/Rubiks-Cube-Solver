from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self.cube = encodedCube
    
    def get(self):
        return self.cube
    
    def rotate(self, directions):
        if directions == 'F':
            self._rotateF()
        else:
            self._rotateF_anti_clockwise()
        return self.cube
    
    
    
    #rotates the cube front face clockwise
    def _rotateF(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
    #rotating the front face of the cube clockwise
        rotatedCubeList[FTR] = cubeList[FTL]
        rotatedCubeList[FMR] = cubeList[FTM]
        rotatedCubeList[FBR] = cubeList[FTR]
        rotatedCubeList[FTM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FBM] = cubeList[FMR]
        rotatedCubeList[FTL] = cubeList[FBL]
        rotatedCubeList[FML] = cubeList[FBM]
        rotatedCubeList[FBL] = cubeList[FBR]
    #rotating right to down
        rotatedCubeList[DTR] = cubeList[RTL]
        rotatedCubeList[DTM] = cubeList[RML]
        rotatedCubeList[DTL] = cubeList[RBL]
    #rotating left to up
        rotatedCubeList[UBR] = cubeList[LTR]
        rotatedCubeList[UBM] = cubeList[LMR]
        rotatedCubeList[UBL] = cubeList[LBR]
    #rotating up to right
        rotatedCubeList[RTL] = cubeList[UBL]
        rotatedCubeList[RML] = cubeList[UBM]
        rotatedCubeList[RBL] = cubeList[UBR]
    #rotating down to left
        rotatedCubeList[LTR] = cubeList[DTL]
        rotatedCubeList[LMR] = cubeList[DTM]
        rotatedCubeList[LBR] = cubeList[DTR]
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)
        
        
    #rotates the cubes front face anti-clockwise    
    def _rotateF_anti_clockwise(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
    #rotating the front face of the cube anti-clockwise
        rotatedCubeList[FBL] = cubeList[FTL]
        rotatedCubeList[FML] = cubeList[FTM]
        rotatedCubeList[FTL] = cubeList[FTR]
        rotatedCubeList[FBM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FTM] = cubeList[FMR]
        rotatedCubeList[FBR] = cubeList[FBL]
        rotatedCubeList[FMR] = cubeList[FBM]
        rotatedCubeList[FTR] = cubeList[FBR]
        
    #rotating right to up
        rotatedCubeList[UBL] = cubeList[RTL]
        rotatedCubeList[UBM] = cubeList[RML]
        rotatedCubeList[UBR] = cubeList[RBL]
        
    #rotating left to down
        rotatedCubeList[DTL] = cubeList[LTR]
        rotatedCubeList[DTM] = cubeList[LMR]
        rotatedCubeList[DTR] = cubeList[LBR]
        
    #rotating up to left
        rotatedCubeList[LBR] = cubeList[UBL]
        rotatedCubeList[LMR] = cubeList[UBM]
        rotatedCubeList[LTR] = cubeList[UBR]
        
    #rotating down to right
        rotatedCubeList[RTL] = cubeList[DTL]
        rotatedCubeList[RML] = cubeList[DTM]
        rotatedCubeList[RBL] = cubeList[DTR]
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)

        