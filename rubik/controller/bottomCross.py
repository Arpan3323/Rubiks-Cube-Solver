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
    cubeList = theCube.get()
    topEdges = [(cubeList[UTM], 'B'), (cubeList[UML], 'L'), 
                (cubeList[UMR], 'R'), (cubeList[UBM], 'F')]
    
    faceEdges = [(cubeList[FTM], cubeList[FML], cubeList[FMR], cubeList[FBM], 'F'), 
                (cubeList[RTM], cubeList[RML], cubeList[RMR], cubeList[RBM], 'R'),
                (cubeList[BTM], cubeList[BML], cubeList[BMR], cubeList[BBM], 'B'),
                (cubeList[LTM], cubeList[LML], cubeList[LMR], cubeList[LBM], 'L')]

    if daisyEdge == 3:
        for missingEdge in topEdges:
            if missingEdge[0] != cubeList[DMM]:
                edgeNeeded = missingEdge[0]
                missingEdgeAdjacentFace = missingEdge[1]
             
        for edge in faceEdges:
            if (edge[0] == cubeList[DMM]):
                edgeFace = edge[4]
                edgeLocation = edge[0]
            
            elif (edge[1] == cubeList[DMM]):
                edgeFace = edge[4]
                edgeLocation = edge[1]
                
            elif (edge[2] == cubeList[DMM]):
                edgeFace = edge[4]
                edgeLocation = edge[2]
    
            elif (edge[3] == cubeList[DMM]):
                edgeFace = edge[4]
                edgeLocation = edge[3]

            
        #if the needed edge is on front face
        if edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[FMR]:
            rotation += 'uR'
            cubeList = list(theCube.rotate(rotation))
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[FML]:
            rotation += 'FFuR'
            cubeList = list(theCube.rotate(rotation))
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[FTM]:
            rotation += 'FuR'
            cubeList = list(theCube.rotate(rotation))
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[FBM]:
            rotation += 'fuR'
            cubeList = list(theCube.rotate(rotation))
            
        #if needed edge is on the right face
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[RBM]:
            rotation += 'Rfr'
            cubeList = list(theCube.rotate(rotation))
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[RML]:
            rotation += 'f'
            cubeList = list(theCube.rotate(rotation))
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[RMR]:
            rotation += 'uuB'
            cubeList = list(theCube.rotate(rotation))
        #if needed edge is on the back face
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[BML]:
            rotation += 'ur'
            cubeList = list(theCube.rotate(rotation))
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[BMR]:
            rotation += 'UL'
            cubeList = list(theCube.rotate(rotation))
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[BBM]:
            rotation += 'UUbul'
            cubeList = list(theCube.rotate(rotation))
        #if needed edge is on the left face
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[LML]:
            rotation += 'UUb'
            cubeList = list(theCube.rotate(rotation))
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[LBM]:
            rotation += 'ULUb'
            cubeList = list(theCube.rotate(rotation))
        elif edgeNeeded == cubeList[UBM] and edgeLocation == cubeList[LMR]:
            rotation += 'F'
            cubeList = list(theCube.rotate(rotation))
        
    
    #after daisy is formed on top, side edges will be aligned and rotated to form bottom cross         
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
         
    
    