from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    cubeList = list(Cube.get(self))
    cubeUpCenter = cubeList[UMM]
    cubeDownCenter = cubeList[DMM]         
       
    if _verifyBottomCrossExists(theCube):
        return ''
    
    #checking if top-daisy exists
    topEdges = [cubeList[UTM], cubeList[UML], cubeList[UMR], cubeList[UBM]]
    
    daisyEdge = 0
    topDaisyFound = False
    verticalEdgesAlignedOnTop = False
    for edges in topEdges:
        if edges == cubeDownCenter:
            daisyEdge += 1
            
    if daisyEdge == 4:
        topDaisyFound = True
        
    #check if edges are aligned with vertical center faces
    if  (cubeList[FTM] == cubeList[FMM]) and (cubeList[RTM] == cubeList[RMM]) and (cubeList[BTM] == cubeList[BMM]) and (cubeList[LTM] == cubeList[LMM]):
        verticalEdgesAlignedOnTop = True
        
    if (topDaisyFound == True) and (verticalEdgesAlignedOnTop == True):
        return 'FFRRBBLL'
    else: 
        return 'FRRBBLL'
    
    
    return 'F'      #TODO:  remove this stubbed value


#method to check if the incoming cubeList already has a bottom cross
def _verifyBottomCrossExists(cube):
    cube = cube.get()
    cubeList = list(cube)
    if cubeList[48] != cubeList[49]:
        return False
    if cubeList[46] != cubeList[49]:
        return False
    if cubeList[52] != cubeList[49]:
        return False
    if cubeList[50] != cubeList[49]:
        return False
    if cubeList[31] != cubeList[34]:
        return False
    if cubeList[4] != cubeList[7]:
        return False
    if cubeList[13] != cubeList[16]:
        return False
    if cubeList[22] != cubeList[25]:
        return False
    if cubeList[49] != cubeList[48]:
        return False
    return True
