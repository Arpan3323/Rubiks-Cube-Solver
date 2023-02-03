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
        
        #defaulting direction to F if direction is missing or empty
        if directions == None or directions == "":
            directions = 'F'
        
        directionList = list(directions)
        for direction in directionList:
            
            rotatedCube = ""
            
            if direction == 'F':
                rotatedCube = self._rotateF()
                
            elif(directions == 'f'):
                rotatedCube = self._rotateF_anti_clockwise()
                
            elif(directions == 'R'):
                rotatedCube = self._rotateR()
                
            elif(directions == 'r'):
                rotatedCube = self._rotateR_anti_clockwise()
                
            elif(directions == 'B'):
                rotatedCube = self._rotateB()
            
            elif(directions == 'b'):
                rotatedCube = self._rotateB_anti_clockwise()
            
            elif(directions == 'L'):
                rotatedCube = self._rotateL()
                
            elif(directions == 'l'):
                rotatedCube = self._rotateL_anti_clockwise()
            
            elif(directions == 'U'):
                rotatedCube = self._rotateU()
                
            elif(directions == 'u'):
                rotatedCube = self._rotateU_anti_clockwise()
                
        return rotatedCube
    
    
    
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
        
    #rotating the left face of the cube clockwise
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
        
        
    #rotates the cubes left face anti-clockwise
    def _rotateL_anti_clockwise(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        
    #rotating the left face of the cube anti-clockwise
        rotatedCubeList[LTL] = cubeList[LTR]
        rotatedCubeList[LTM] = cubeList[LMR]
        rotatedCubeList[LTR] = cubeList[LBR]
        rotatedCubeList[LML] = cubeList[LTM]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LMR] = cubeList[LBM]
        rotatedCubeList[LBL] = cubeList[LTL]
        rotatedCubeList[LBM] = cubeList[LML]
        rotatedCubeList[LBR] = cubeList[LBL]
    
    #rotating front to up
        rotatedCubeList[UTL] = cubeList[FTL]
        rotatedCubeList[UML] = cubeList[FML]
        rotatedCubeList[UBL] = cubeList[FBL]
        
    #rotating up to back
        rotatedCubeList[BTR] = cubeList[UBL]
        rotatedCubeList[BMR] = cubeList[UML]
        rotatedCubeList[BBR] = cubeList[UTL]
        
    #rotating down to front
        rotatedCubeList[FTL] = cubeList[DTL]
        rotatedCubeList[FML] = cubeList[DML]
        rotatedCubeList[FBL] = cubeList[DBL]
        
    #rotating back to down
        rotatedCubeList[DTL] = cubeList[BBR]
        rotatedCubeList[DML] = cubeList[BMR]
        rotatedCubeList[DBL] = cubeList[BTR]
        
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)
        
    #rotating the cubes up face clockwise
    def _rotateU(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        
    #rotating the up face of the cube clockwise
        rotatedCubeList[UTR] = cubeList[UTL]
        rotatedCubeList[UMR] = cubeList[UTM]
        rotatedCubeList[UBR] = cubeList[UTR]
        rotatedCubeList[UTM] = cubeList[UML]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UBM] = cubeList[UMR]
        rotatedCubeList[UTL] = cubeList[UBL]
        rotatedCubeList[UML] = cubeList[UBM]
        rotatedCubeList[UBL] = cubeList[UBR]
    
    #rotating left to back
        rotatedCubeList[BTL] = cubeList[LTL]
        rotatedCubeList[BTM] = cubeList[LTM]
        rotatedCubeList[BTR] = cubeList[LTR]
        
    #rotating back to right
        rotatedCubeList[RTL] = cubeList[BTL]
        rotatedCubeList[RTM] = cubeList[BTM]
        rotatedCubeList[RTR] = cubeList[BTR]
        
    #rotating right to front
        rotatedCubeList[FTL] = cubeList[RTL]
        rotatedCubeList[FTM] = cubeList[RTM]
        rotatedCubeList[FTR] = cubeList[RTR]
        
    #rotating front to left
        rotatedCubeList[LTL] = cubeList[FTL]
        rotatedCubeList[LTM] = cubeList[FTM]
        rotatedCubeList[LTR] = cubeList[FTR]
        
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)
        
        
    #rotating the cubes up face anti-clockwise
    def _rotateU_anti_clockwise(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        
    #rotating the up face of the cube anti-clockwise
        rotatedCubeList[UTL] = cubeList[UTR]
        rotatedCubeList[UTM] = cubeList[UMR]
        rotatedCubeList[UTR] = cubeList[UBR]
        rotatedCubeList[UML] = cubeList[UTM]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UMR] = cubeList[UBM]
        rotatedCubeList[UBL] = cubeList[UTL]
        rotatedCubeList[UBM] = cubeList[UML]
        rotatedCubeList[UBR] = cubeList[UBL]
    
    #rotating back to left
        rotatedCubeList[LTL] = cubeList[BTL]
        rotatedCubeList[LTM] = cubeList[BTM]
        rotatedCubeList[LTR] = cubeList[BTR]
        
    #rotating right to back
        rotatedCubeList[BTL] = cubeList[RTL]
        rotatedCubeList[BTM] = cubeList[RTM]
        rotatedCubeList[BTR] = cubeList[RTR]
        
    #rotating front to right
        rotatedCubeList[RTL] = cubeList[FTL]
        rotatedCubeList[RTM] = cubeList[FTM]
        rotatedCubeList[RTR] = cubeList[FTR]
        
    #rotating left to front
        rotatedCubeList[FTL] = cubeList[LTL]
        rotatedCubeList[FTM] = cubeList[LTM]
        rotatedCubeList[FTR] = cubeList[LTR]
        
    #converting the list to a string
        self.cube = "".join(rotatedCubeList)