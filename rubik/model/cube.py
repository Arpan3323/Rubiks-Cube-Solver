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
        directionList = list(directions)
        for direction in directionList:
            if direction == 'F':
                self._rotateF()
                
            elif(directions == 'f'):
                self._rotateF_anti_clockwise()
                
            elif(directions == 'R'):
                self._rotateR()
                
            elif(directions == 'r'):
                self._rotateR_anti_clockwise()
                
            elif(directions == 'B'):
                self._rotateB()
            
            elif(directions == 'b'):
                self._rotateB_anti_clockwise()
                
            else:
                self._rotateL()
                
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
        rotatedCubeList[RML] = cubeList[RBM]
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
        
    #rotating up to back
        rotatedCubeList[BTL] = cubeList[UBR]
        rotatedCubeList[BML] = cubeList[UMR]
        rotatedCubeList[BBL] = cubeList[UTR]
        
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)
        

    #rotates the cubes right face anti-clockwise
    def _rotateR_anti_clockwise(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        
    #rotating the right face of the cube anti-clockwise
        rotatedCubeList[RBL] = cubeList[RTL]
        rotatedCubeList[RML] = cubeList[RTM]
        rotatedCubeList[RTL] = cubeList[RTR]
        rotatedCubeList[RBM] = cubeList[RML]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RTM] = cubeList[RMR]
        rotatedCubeList[RBR] = cubeList[RBL]
        rotatedCubeList[RMR] = cubeList[RBM]
        rotatedCubeList[RTR] = cubeList[RBR]
    
    #rotating back to up
        rotatedCubeList[UBR] = cubeList[BTL]
        rotatedCubeList[UMR] = cubeList[BML]
        rotatedCubeList[UTR] = cubeList[BBL]
        
    #rotating front to down
        rotatedCubeList[DTR] = cubeList[FTR]
        rotatedCubeList[DMR] = cubeList[FMR]
        rotatedCubeList[DBR] = cubeList[FBR]
        
    #rotating down to back
        rotatedCubeList[BBL] = cubeList[DTR]
        rotatedCubeList[BML] = cubeList[DMR]
        rotatedCubeList[BTL] = cubeList[DBR]
        
    #rotating up to back
        rotatedCubeList[FBR] = cubeList[UBR]
        rotatedCubeList[FMR] = cubeList[UMR]
        rotatedCubeList[FTR] = cubeList[UTR]
        
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)
    
    #rotates the cubes back face clockwise    
    def _rotateB(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        
    #rotating the back face of the cube clockwise
        rotatedCubeList[BTR] = cubeList[BTL]
        rotatedCubeList[BMR] = cubeList[BTM]
        rotatedCubeList[BBR] = cubeList[BTR]
        rotatedCubeList[BTM] = cubeList[BML]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BBM] = cubeList[BMR]
        rotatedCubeList[BTL] = cubeList[BBL]
        rotatedCubeList[BML] = cubeList[BBM]
        rotatedCubeList[BBL] = cubeList[BBR]
    
    #rotating up to left
        rotatedCubeList[LBL] = cubeList[UTL]
        rotatedCubeList[LML] = cubeList[UTM]
        rotatedCubeList[LTL] = cubeList[UTR]
        
    #rotating left to down
        rotatedCubeList[DBL] = cubeList[LTL]
        rotatedCubeList[DBM] = cubeList[LML]
        rotatedCubeList[DBR] = cubeList[LBL]
        
    #rotating down to right
        rotatedCubeList[RBR] = cubeList[DBL]
        rotatedCubeList[RMR] = cubeList[DBM]
        rotatedCubeList[RTR] = cubeList[DBR]
        
    #rotating right to up
        rotatedCubeList[UTL] = cubeList[RTR]
        rotatedCubeList[UTM] = cubeList[RMR]
        rotatedCubeList[UTR] = cubeList[RBR]
        
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)
     
     
    #rotates the cubes back face anti-clockwise    
    def _rotateB_anti_clockwise(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        
    #rotating the back face of the cube anti-clockwise
        rotatedCubeList[BBL] = cubeList[BTL]
        rotatedCubeList[BML] = cubeList[BTM]
        rotatedCubeList[BTL] = cubeList[BTR]
        rotatedCubeList[BBM] = cubeList[BML]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BTM] = cubeList[BMR]
        rotatedCubeList[BBR] = cubeList[BBL]
        rotatedCubeList[BMR] = cubeList[BBM]
        rotatedCubeList[BTR] = cubeList[BBR]
    
    #rotating up to right
        rotatedCubeList[RTR] = cubeList[UTL]
        rotatedCubeList[RMR] = cubeList[UTM]
        rotatedCubeList[RBR] = cubeList[UTR]
        
    #rotating left to up
        rotatedCubeList[UTR] = cubeList[LTL]
        rotatedCubeList[UTM] = cubeList[LML]
        rotatedCubeList[UTL] = cubeList[LBL]
        
    #rotating down to right
        rotatedCubeList[LTL] = cubeList[DBL]
        rotatedCubeList[LML] = cubeList[DBM]
        rotatedCubeList[LBL] = cubeList[DBR]
        
    #rotating right to down
        rotatedCubeList[DBR] = cubeList[RTR]
        rotatedCubeList[DBM] = cubeList[RMR]
        rotatedCubeList[DBL] = cubeList[RBR]
        
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)


    #rotates the cubes left face clockwise
    def _rotateL(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        
    #rotating the back face of the cube anti-clockwise
        rotatedCubeList[LTR] = cubeList[LTL]
        rotatedCubeList[LMR] = cubeList[LTM]
        rotatedCubeList[LBR] = cubeList[LTR]
        rotatedCubeList[LTM] = cubeList[LML]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LBM] = cubeList[LMR]
        rotatedCubeList[LTL] = cubeList[LBL]
        rotatedCubeList[LML] = cubeList[LBM]
        rotatedCubeList[LBL] = cubeList[LBR]
    
    #rotating up to front
        rotatedCubeList[FTL] = cubeList[UTL]
        rotatedCubeList[FML] = cubeList[UML]
        rotatedCubeList[FBL] = cubeList[UBL]
        
    #rotating back to up
        rotatedCubeList[UBL] = cubeList[BTR]
        rotatedCubeList[UML] = cubeList[BMR]
        rotatedCubeList[UTL] = cubeList[BBR]
        
    #rotating front to down
        rotatedCubeList[DTL] = cubeList[FTL]
        rotatedCubeList[DML] = cubeList[FML]
        rotatedCubeList[DBL] = cubeList[FBL]
        
    #rotating down to back
        rotatedCubeList[BBR] = cubeList[DTL]
        rotatedCubeList[BMR] = cubeList[DML]
        rotatedCubeList[BTR] = cubeList[DBL]
        
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)