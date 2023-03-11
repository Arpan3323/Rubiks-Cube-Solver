from rubik.model.constants import *
from rubik.model.cube import Cube
import rubik.controller.bottomCross as bc

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''  
    cubeList = list(theCube.get())
    
    if _verifyBottomLayerExists(cubeList):
        return ''
    
    if bc._verifyBottomCrossExists(cubeList) == False:
        cubeList = alignToBottomCross(theCube)
    
    rotations = ''    
    if _verifyBottomLayerExists(cubeList) == False:
       cubeList, rotations = rotateTopLayerPieceToBottom(cubeList)
       
    
    return rotations

def _verifyBottomLayerExists(cubeList):
    bottomLayerExists = ((cubeList[FMM] in cubeList[FBL:FBR+1])and (cubeList[RMM] in cubeList[RBL:RBR+1]) and 
                        (cubeList[BMM] in cubeList[BBL:BBR+1]) and (cubeList[LMM] in cubeList[LBL:LBR+1]) and
                        (cubeList[DMM] in cubeList[DTL:DTR+1]) and (cubeList[DMM] in cubeList[DBL:DBR+1]) and
                        (cubeList[DMM] in cubeList[DML]) and (cubeList[DMM] in cubeList[DMR]))
    return bottomLayerExists 

def alignToBottomCross(theCube):
    bottomCrossRotations = bc.solveBottomCross(theCube)
    bottomCrossCubeList = list(theCube.get())
    return bottomCrossCubeList

def rotateTopLayerPieceToBottom(cubeList):
    TopLayerPieceToBottomRotations = ''
    
    if (cubeList[DMM] in cubeList[FTL:FTR+1]) or (cubeList[DMM] in cubeList[RTL:RTR+1]) or (cubeList[DMM] in cubeList[BTL:BTR+1]) or (cubeList[DMM] in cubeList[LTL:LTR+1]):
        cubeList, TopLayerPieceToBottomRotations, triggerPieceLocation = alignTopLayerPieceWithCenter(cubeList)
        
    if (triggerPieceLocation == FTL) or (triggerPieceLocation == RTL) or (triggerPieceLocation == BTL) or (triggerPieceLocation == LTL):
        cubeList = Cube(''.join(cubeList)).leftTrigger(triggerPieceLocation)[0]
        TopLayerPieceToBottomRotations += Cube(''.join(cubeList)).leftTrigger(triggerPieceLocation)[1]
        
    return cubeList, TopLayerPieceToBottomRotations


def alignTopLayerPieceWithCenter(cubeList):
    topCornerPairs = [(FTL, LTR), (FTR, RTL), (RTR, BTL), (BTR, LTL)]
    requiredTopLayerPiece = ''
    topLayerPieceToAlignWithCenter = ''
    alignTopLayerRotations = ''
    
    for pair in topCornerPairs:
        if cubeList[pair[0]] == cubeList[DMM]: 
            requiredTopLayerPiece = pair[0]
            topLayerPieceToAlignWithCenter = pair[1]
        elif cubeList[pair[1]] == cubeList[DMM]: 
            requiredTopLayerPiece = pair[1]
            topLayerPieceToAlignWithCenter = pair[0]
    
    if cubeList[topLayerPieceToAlignWithCenter] == cubeList[FMM]:
        while(cubeList[topLayerPieceToAlignWithCenter] != cubeList[FTR] and cubeList[topLayerPieceToAlignWithCenter] != cubeList[FTL]):
            topLayerPieceToAlignWithCenter = pieceLocationAfterRotation(topLayerPieceToAlignWithCenter)
            cubeList =  list(Cube(''.join(cubeList)).rotate('u'))
            alignTopLayerRotations += 'u'
        
    elif cubeList[topLayerPieceToAlignWithCenter] == cubeList[RMM]:
        while(cubeList[topLayerPieceToAlignWithCenter] != cubeList[RTR] and cubeList[topLayerPieceToAlignWithCenter] != cubeList[RTL]):
            topLayerPieceToAlignWithCenter = pieceLocationAfterRotation(topLayerPieceToAlignWithCenter)
            cubeList =  list(Cube(''.join(cubeList)).rotate('u'))
            alignTopLayerRotations += 'u'
   
    elif cubeList[topLayerPieceToAlignWithCenter] == cubeList[BMM]:
        while(cubeList[topLayerPieceToAlignWithCenter] != cubeList[BTR] and cubeList[topLayerPieceToAlignWithCenter] != cubeList[BTL]):
            topLayerPieceToAlignWithCenter = pieceLocationAfterRotation(topLayerPieceToAlignWithCenter)
            cubeList =  list(Cube(''.join(cubeList)).rotate('u'))
            alignTopLayerRotations += 'u'
   
    elif cubeList[topLayerPieceToAlignWithCenter] == cubeList[LMM]:
        while(cubeList[topLayerPieceToAlignWithCenter] != cubeList[LTR] and cubeList[topLayerPieceToAlignWithCenter] != cubeList[LTL]):
            topLayerPieceToAlignWithCenter = pieceLocationAfterRotation(topLayerPieceToAlignWithCenter)
            cubeList =  list(Cube(''.join(cubeList)).rotate('u'))
            alignTopLayerRotations += 'u'

    return cubeList, alignTopLayerRotations, topLayerPieceToAlignWithCenter

def pieceLocationAfterRotation(topLayerPieceToAlignWithCenter):
    if topLayerPieceToAlignWithCenter == LTL:
        topLayerPieceToAlignWithCenter = FTL  
        
    elif topLayerPieceToAlignWithCenter == LTR:
        topLayerPieceToAlignWithCenter = FTR
        
    else:
        topLayerPieceToAlignWithCenter += 9
        
    return topLayerPieceToAlignWithCenter


        
    
