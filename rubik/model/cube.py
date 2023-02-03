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
            
        elif(directions == 'f'):
            self._rotateF_anti_clockwise()
        else:
            self._rotateR()
            
        return self.cube
    
    
    
    #rotates the cubes front face clockwise
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
        rotatedCubeList[RBL] = cubeList[DTL]
        rotatedCubeList[RML] = cubeList[DTM]
        rotatedCubeList[RTL] = cubeList[DTR]
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)
        
    #rotates the cubes right face clockwise
    def _rotateR(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
    #rotating the right face of the cube clockwise
        rotatedCubeList[FTR] = cubeList[RTL]
        rotatedCubeList[FMR] = cubeList[RTM]
        rotatedCubeList[FBR] = cubeList[RTR]
        rotatedCubeList[RTM] = cubeList[RML]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RBM] = cubeList[RMR]
        rotatedCubeList[RTL] = cubeList[RBL]
        rotatedCubeList[FML] = cubeList[RBM]
        rotatedCubeList[RBL] = cubeList[RBR]
    
    #rotating back to down
        rotatedCubeList[DBR] = cubeList[BTL]
        rotatedCubeList[DMR] = cubeList[BML]
        rotatedCubeList[DTR] = cubeList[BBL]
        
    #rotating front to up
        rotatedCubeList[UTR] = cubeList[FTR]
        rotatedCubeList[UMR] = cubeList[FMR]
        rotatedCubeList[UBR] = cubeList[FBR]
        
    #rotating down to front
        rotatedCubeList[FTR] = cubeList[DTR]
        rotatedCubeList[FMR] = cubeList[DMR]
        rotatedCubeList[FBR] = cubeList[DBR]
        
    #rotating top to back
        rotatedCubeList[BTL] = cubeList[UBR]
        rotatedCubeList[BML] = cubeList[UMR]
        rotatedCubeList[BBL] = cubeList[UTR]
        
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)
        

        