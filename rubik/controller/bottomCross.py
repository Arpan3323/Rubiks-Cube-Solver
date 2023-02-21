from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    
    cubeList = theCube.get()
    cubeUpCenter = cubeList[UMM]
    cubeDownCenter = cubeList[DMM]
    daisyPetals = 4
    rotation = ''       
       
    if _verifyBottomCrossExists(cubeList):
        return ''
    
    topEdges = [cubeList[UTM], cubeList[UML], cubeList[UMR], cubeList[UBM]]
    sideEdges = [cubeList[FTM], cubeList[RTM], cubeList[BTM], cubeList[LTM]]
    
    #checking if top-daisy exists and side edges are aligned
    daisyEdge = topEdges.count(cubeDownCenter)
    topDaisyFound = daisyEdge == daisyPetals
    
    #check if side edges are aligned on top
    sideEdgesAlignedOnTop = (sideEdges == [cubeList[FMM], cubeList[RMM], cubeList[BMM], cubeList[LMM]])
        
        
    #check if top daisy exists but side edges are not aligned
    if (topDaisyFound == True) and (sideEdgesAlignedOnTop == False):
        return _daisyExistsAndSideEdgesUnaligned(theCube)
        
    #checks if daisy exists and side edges are aligned
    if (topDaisyFound == True) and (sideEdgesAlignedOnTop == True):
        return 'FFRRBBLL'
    
    #checks if neither daisy exists nor side edges are aligned 
    if (topDaisyFound == False) and (sideEdgesAlignedOnTop == False):
        #return _daisyExistsAndSideEdgesUnaligned(_daisyFormation(daisyEdge, theCube))
        return _daisyFormation(daisyEdge, theCube)
        
    
    '''#checking if front face has been rotated once to form bottom cross
    
    topEdgePairs = [(cubeList[UBM], cubeList[FTM], 'F'),
                    (cubeList[UMR], cubeList[RTM], 'R'),
                    (cubeList[UTM], cubeList[BTM], 'B'),
                    (cubeList[UML], cubeList[LTM], 'L')]
    
    rotation = ''
    
    if (cubeList[RML] == cubeDownCenter) and (cubeList[FMR] == cubeList[FMM]):
        rotation += 'F'
    
    if (cubeList[BML] == cubeDownCenter) and (cubeList[RMR] == cubeList[RMM]):
        rotation += 'R'
        
    if (cubeList[LML] == cubeDownCenter) and (cubeList[BMR] == cubeList[BMM]):
        rotation += 'B'
        
    if (cubeList[FML] == cubeDownCenter) and (cubeList[LMR] == cubeList[LMM]):
        rotation += 'L'
    
    for edge in topEdgePairs:
        if (edge[0] == cubeDownCenter) and (edge[1] == cubeList[FMM]):
            rotation += 'FF'
                
        elif (edge[0] == cubeDownCenter) and (edge[1] == cubeList[RMM]):
            rotation += 'RR'
            
        elif (edge[0] == cubeDownCenter) and (edge[1] == cubeList[BMM]):
            rotation += 'BB'
                
        elif (edge[0] == cubeDownCenter) and (edge[1] == cubeList[LMM]):
            rotation += 'LL'
    return rotation'''


#return true if the bottom cross exists otherwise return false
def _verifyBottomCrossExists(cubeList):
    return (cubeList[DML] == cubeList[DMM] and cubeList[DTM] == cubeList[DMM] and cubeList[DBM] == cubeList[DMM]
    and cubeList[DMR] == cubeList[DMM] and cubeList[LMM] == cubeList[LBM] and cubeList[FMM] == cubeList[FBM]
    and cubeList[RMM] == cubeList[RBM] and cubeList[BMM] == cubeList[BBM])
    

def _daisyExistsAndSideEdgesUnaligned(theCube):
    rotation = ''
    cubeList = theCube.get()
    #front face
    while(cubeList[FTM] != cubeList[FMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[FTM] == cubeList[FMM]):
        rotation += 'FF'
    #right face
    while(cubeList[RTM] != cubeList[RMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[RTM] == cubeList[RMM]):
        rotation += 'RR'
    #back face
    while(cubeList[BTM] != cubeList[BMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[BTM] == cubeList[BMM]):
        rotation += 'BB'
    #left face
    while(cubeList[LTM] != cubeList[LMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[LTM] == cubeList[LMM]):
        rotation += 'LL'
    return rotation

#forms a daisy on top
def _daisyFormation(daisyEdge, theCube):
    rotation = ''
    if daisyEdge == 3:
        rotation += 'Rfr'
        cubeList = list(theCube.rotate(rotation))
    while(cubeList[FTM] != cubeList[FMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[FTM] == cubeList[FMM]):
        rotation += 'FF'
    #right face
    while(cubeList[RTM] != cubeList[RMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[RTM] == cubeList[RMM]):
        rotation += 'RR'
    #back face
    while(cubeList[BTM] != cubeList[BMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[BTM] == cubeList[BMM]):
        rotation += 'BB'
    #left face
    while(cubeList[LTM] != cubeList[LMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[LTM] == cubeList[LMM]):
        rotation += 'LL'
    return rotation
         
    
    