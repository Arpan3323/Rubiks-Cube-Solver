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
        rotation = 'FFRRBBLL'
        theCube.rotate(rotation)
        return rotation
    
    #checks if daisy exists nor side edges are aligned 
    if (topDaisyFound == False):
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
    topEdges = [cubeList[UBM], cubeList[UMR], cubeList[UTM], cubeList[UML]]
    
    if daisyEdge <= 3 and topEdges[0] != cubeList[DMM]:
        rotation += _alignDaisyBottomEdge(theCube)
        
    cubeList = list(theCube.rotate(rotation))
    
    
    '''missingEdgeList = []
    edgeLocationList = []

    if daisyEdge <= 3:
        
        for missingEdge in topEdges:
            if missingEdge[0] != cubeList[DMM]:
                edgeNeeded = missingEdge[0]
                missingEdgeList.append(edgeNeeded)
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

        #rotating the top if only edge is missing so that missing daisy edge is on UBM
        if len(missingEdgeList) == 1:
            while(missingEdgeList[0] == cubeList[UML] 
                  or missingEdgeList[0] == cubeList[UMR] 
                  or missingEdgeList[0] == cubeList[UTM]):
                cubeList = list(theCube.rotate('u'))
                
                
                
        
        if edgeNeeded == cubeList[UBM]:
            
            #if the needed edge is on front face 
            if edgeLocation == cubeList[FMR]:
                rotation += 'uR'#U
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[FML]:
                rotation += 'FFuR'#u
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[FTM]:
                rotation += 'FuR'#U
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[FBM]:
                rotation += 'fuR'#U
                cubeList = list(theCube.rotate(rotation))
                
            #if needed edge is on the right face
            elif edgeLocation == cubeList[RBM]:
                rotation += 'Rfr'#remove r
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[RML]:
                rotation += 'f'
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[RMR]:
                rotation += 'uuB'#uu
                cubeList = list(theCube.rotate(rotation))
            #if needed edge is on the back face
            elif edgeLocation == cubeList[BML]:
                rotation += 'ur'#U
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[BMR]:
                rotation += 'UL'#u
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[BBM]:
                rotation += 'UUbul'#u
                cubeList = list(theCube.rotate(rotation))
            #if needed edge is on the left face
            elif edgeLocation == cubeList[LML]:
                rotation += 'UUb'
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[LBM]:
                rotation += 'ULUb'
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[LMR]:
                rotation += 'F'
                cubeList = list(theCube.rotate(rotation))
            #if needed edge is on the down face
            elif edgeLocation == cubeList[DTM]:
                rotation += 'FF'
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[DML]:
                rotation += 'ULL'
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[DMR]:
                rotation += 'uRR'
                cubeList = list(theCube.rotate(rotation))
            elif edgeLocation == cubeList[DBM]:
                rotation += 'UUBB'
                cubeList = list(theCube.rotate(rotation))'''
            
    #after daisy is formed on top, side edges will be aligned and rotated to form bottom cross
    #front face         
    while(cubeList[FTM] != cubeList[FMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[FTM] == cubeList[FMM]):
        rotation += 'FF'
        cubeList = list(theCube.rotate('FF'))
    #right face
    while(cubeList[RTM] != cubeList[RMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[RTM] == cubeList[RMM]):
        rotation += 'RR'
        cubeList = list(theCube.rotate('RR'))
    #back face
    while(cubeList[BTM] != cubeList[BMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[BTM] == cubeList[BMM]):
        rotation += 'BB'
        cubeList = list(theCube.rotate('BB'))
    #left face
    while(cubeList[LTM] != cubeList[LMM]):
        rotation += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[LTM] == cubeList[LMM]):
        rotation += 'LL'
        cubeList = list(theCube.rotate('LL'))
    return rotation

def _alignDaisyBottomEdge(theCube):
    rotation = ''
    cubeList = theCube.get()
    edgeLocation = []
    
    faceEdges = [(cubeList[FTM], cubeList[FML], cubeList[FMR], cubeList[FBM], 'F'), 
                (cubeList[RTM], cubeList[RML], cubeList[RMR], cubeList[RBM], 'R'),
                (cubeList[BTM], cubeList[BML], cubeList[BMR], cubeList[BBM], 'B'),
                (cubeList[LTM], cubeList[LML], cubeList[LMR], cubeList[LBM], 'L'),
                (cubeList[DTM], cubeList[DML], cubeList[DMR], cubeList[DBM], 'D')]
    
    for edge in faceEdges:
        if (edge[0] == cubeList[DMM]) and len(edgeLocation) == 0:
            edgeFace = edge[4]
            edgeLocation.append(edge[0])
            
        elif (edge[1] == cubeList[DMM]) and len(edgeLocation) == 0:
            edgeFace = edge[4]
            edgeLocation.append(edge[1]) 
            
        elif (edge[2] == cubeList[DMM]) and len(edgeLocation) == 0:
            edgeFace = edge[4]
            edgeLocation.append(edge[2]) 

        elif (edge[3] == cubeList[DMM]) and len(edgeLocation) == 0:
            edgeFace = edge[4]
            edgeLocation.append(edge[3])
            
    #if needed edge is on the right face
    if edgeLocation[0] == cubeList[RBM]:
        rotation += 'uRUf'
        #cubeList = list(theCube.rotate(rotation))
    elif edgeLocation[0] == cubeList[RML]:
        rotation += 'f'
        #cubeList = list(theCube.rotate(rotation))
    elif edgeLocation[0] == cubeList[RMR]:
        rotation += 'uRRUf'
        #cubeList = list(theCube.rotate(rotation))   
    #if the edge is found here that means, the petal does not exist on UMR as well
    elif edgeLocation[0] == cubeList[RTM]:
        rotation += 'rf'
        #cubeList = list(theCube.rotate(rotation))
    

        
    
    
    return rotation
         
    
    