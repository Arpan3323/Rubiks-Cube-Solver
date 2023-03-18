from rubik.model.constants import *
from rubik.model.cube import Cube
import rubik.controller.bottomCross as bc

def solveBottomLayer(theCube: Cube) -> str:
    cubeList = list(theCube.get())
    
    if verifyBottomLayerExists(cubeList):
        return ''
    
    if bc.verifyBottomCrossExists(cubeList) == False:
        cubeList = _alignToBottomCross(theCube)
    
    rotations = ''
    rotationsIfAPieceIsLeftOnTop = ''
     
    if verifyBottomLayerExists(cubeList) == False:
        
        cubeList, TopLayerToBottomrotations = _rotateTopLayerPieceToBottom(cubeList)
        cubeList, topFaceToSideRotations = _rotatePieceFromTopFaceToSideFace(cubeList)
        cubeList, bottomLayerRotations = _rotateBottomLayerPieceToTopFace(cubeList)
        
        #in some cases, a corner piece is left on top even after above code is executed
        #the while loop below handles that
        while cubeList[DMM] in cubeList[UTL:UTR+1] or cubeList[DMM] in cubeList[UBL:UBR+1]:
            cubeList, rotationsIfAPieceIsLeftOnTop = _rotatePieceFromTopFaceToSideFace(cubeList)
            
        rotations += TopLayerToBottomrotations + topFaceToSideRotations + \
         bottomLayerRotations + rotationsIfAPieceIsLeftOnTop
       
    
    return cubeList, rotations

def verifyBottomLayerExists(cubeList):
    allPiecesFound = 3
    return (
        (cubeList[FBL : FBR + 1].count(cubeList[FMM]) == allPiecesFound)
        and (cubeList[RBL : RBR + 1].count(cubeList[RMM]) == allPiecesFound)
        and (cubeList[BBL : BBR + 1].count(cubeList[BMM]) == allPiecesFound)
        and (cubeList[LBL : LBR + 1].count(cubeList[LMM]) == allPiecesFound)
        and (cubeList[DTL : DTR + 1].count(cubeList[DMM]) == allPiecesFound)
        and (cubeList[DBL : DBR + 1].count(cubeList[DMM]) == allPiecesFound)
        and (cubeList[DMM] == cubeList[DML])
        and (cubeList[DMM] == cubeList[DMR])
    ) 

def _alignToBottomCross(theCube):
    bottomCrossRotations = bc.solveBottomCross(theCube)
    return list(theCube.get())

def _rotatePieceFromTopFaceToSideFace(cubeList):
    topAndDownStackedCorners = [(UTL, DBL), (UTR, DBR), (UBL, DTL), (UBR, DTR)]
    rotationsBeforeTrigger = ''
    rotationsAfterTrigger = ''
    topToSideRotations = ''

    for corners in topAndDownStackedCorners:
        if cubeList[corners[0]] == cubeList[DMM]:
            if (cubeList[corners[1]] != cubeList[DMM]):
                cubeList, rotationsWhenPiecesAreStacked = Cube(''.join(cubeList)).rightTrigger(corners[0])
                topToSideRotations += rotationsWhenPiecesAreStacked
            else:
                downFaceCorner = corners[1]
                cornerToRotate = corners[0]
                while cubeList[cornerToRotate] == cubeList[downFaceCorner]:
                    cornerToRotate, downFaceCorner = _stackedCornerLocation(downFaceCorner, cornerToRotate)
                    rotationsBeforeTrigger += 'U'
                    cubeList = Cube(''.join(cubeList)).rotate('U')
                cubeList, returnedRotations = Cube(''.join(cubeList)).rightTrigger(cornerToRotate)
                rotationsAfterTrigger += returnedRotations
                topToSideRotations += rotationsBeforeTrigger + rotationsAfterTrigger
    cubeList, topLayerRotations = _rotateTopLayerPieceToBottom(cubeList)
    topToSideRotations += topLayerRotations

    return cubeList, topToSideRotations

#After the top face is rotated 'U' this finction returns the new location of the corner piece as well as the new location
#of the down face corner piece that is right below the top face corner piece
def _stackedCornerLocation(downFaceCorner, cornerToRotate):
    if cornerToRotate == UTL:
        cornerToRotate = UTR
    elif cornerToRotate == UTR:
        cornerToRotate = UBR
    elif cornerToRotate == UBR:
        cornerToRotate = UBL
    elif cornerToRotate == UBL:
        cornerToRotate = UTL
                    
    if downFaceCorner == DBL:
        downFaceCorner = DBR
    elif downFaceCorner == DBR:
        downFaceCorner = DTR
    elif downFaceCorner == DTR:
        downFaceCorner = DTL
    elif downFaceCorner == DTL:
        downFaceCorner = DBL
    return cornerToRotate, downFaceCorner

def _rotateTopLayerPieceToBottom(cubeList):
    TopLayerPieceToBottomRotations = ''

    while ((cubeList[DMM] in cubeList[FTL:FTR+1]) 
           or (cubeList[DMM] in cubeList[RTL:RTR+1]) 
           or (cubeList[DMM] in cubeList[BTL:BTR+1]) 
           or (cubeList[DMM] in cubeList[LTL:LTR+1])):
        cubeList, returnedRotations, triggerPieceLocation = _alignTopLayerPieceWithCenter(cubeList)
        TopLayerPieceToBottomRotations += returnedRotations

        if triggerPieceLocation in [FTL, RTL, BTL, LTL]:
            cubeList, returnedRotations = Cube(''.join(cubeList)).leftTrigger(triggerPieceLocation)
            TopLayerPieceToBottomRotations += returnedRotations

        elif triggerPieceLocation in [FTR, RTR, BTR, LTR]:
            cubeList, returnedRotations = Cube(''.join(cubeList)).rightTrigger(triggerPieceLocation)
            TopLayerPieceToBottomRotations += returnedRotations

    return cubeList, TopLayerPieceToBottomRotations


def _alignTopLayerPieceWithCenter(cubeList):
    topCornerPairs = [(FTL, LTR), (FTR, RTL), (RTR, BTL), (BTR, LTL)]
    requiredTopLayerPiece = []
    topLayerPieceToAlignWithCenter = ''
    alignTopLayerRotations = ''

    for pair in topCornerPairs:
        if cubeList[pair[0]] == cubeList[DMM] and not requiredTopLayerPiece: 
            requiredTopLayerPiece.append(pair[0])
            topLayerPieceToAlignWithCenter = pair[1]
        elif cubeList[pair[1]] == cubeList[DMM] and not requiredTopLayerPiece: 
            requiredTopLayerPiece.append(pair[1])
            topLayerPieceToAlignWithCenter = pair[0]
    
    cubeList, topLayerPieceToAlignWithCenter, alignTopLayerRotations = _rotateTopLayerPieceToCenter(cubeList, topLayerPieceToAlignWithCenter, alignTopLayerRotations)

    return cubeList, alignTopLayerRotations, topLayerPieceToAlignWithCenter

#rotates the adjacent top layer corner piece to the face with appropriate center so a trigger can be performed 
def _rotateTopLayerPieceToCenter(cubeList, topLayerPieceToAlignWithCenter, alignTopLayerRotations):
    if cubeList[topLayerPieceToAlignWithCenter] == cubeList[FMM]:
        while topLayerPieceToAlignWithCenter not in [FTR, FTL]:
            topLayerPieceToAlignWithCenter = _pieceLocationAfterRotation(topLayerPieceToAlignWithCenter)
            cubeList =  list(Cube(''.join(cubeList)).rotate('u'))
            alignTopLayerRotations += 'u'

    elif cubeList[topLayerPieceToAlignWithCenter] == cubeList[RMM]:
        while topLayerPieceToAlignWithCenter not in [RTR, RTL]:
            topLayerPieceToAlignWithCenter = _pieceLocationAfterRotation(topLayerPieceToAlignWithCenter)
            cubeList =  list(Cube(''.join(cubeList)).rotate('u'))
            alignTopLayerRotations += 'u'

    elif cubeList[topLayerPieceToAlignWithCenter] == cubeList[BMM]:
        while topLayerPieceToAlignWithCenter not in [BTR, BTL]:
            topLayerPieceToAlignWithCenter = _pieceLocationAfterRotation(topLayerPieceToAlignWithCenter)
            cubeList =  list(Cube(''.join(cubeList)).rotate('u'))
            alignTopLayerRotations += 'u'

    elif cubeList[topLayerPieceToAlignWithCenter] == cubeList[LMM]:
        while topLayerPieceToAlignWithCenter not in [LTR, LTL]:
            topLayerPieceToAlignWithCenter = _pieceLocationAfterRotation(topLayerPieceToAlignWithCenter)
            cubeList =  list(Cube(''.join(cubeList)).rotate('u'))
            alignTopLayerRotations += 'u'
    return cubeList,topLayerPieceToAlignWithCenter, alignTopLayerRotations

def _pieceLocationAfterRotation(topLayerPieceToAlignWithCenter):
    if topLayerPieceToAlignWithCenter == LTL:
        topLayerPieceToAlignWithCenter = FTL  
        
    elif topLayerPieceToAlignWithCenter == LTR:
        topLayerPieceToAlignWithCenter = FTR
        
    else:
        topLayerPieceToAlignWithCenter += 9
        
    return topLayerPieceToAlignWithCenter


def _rotateBottomLayerPieceToTopFace(cubeList):
    bottomLayerToTopFaceRotations = ''
    cornerPieces = [FBL, FBR, RBL, RBR, BBL, BBR, LBL, LBR]
    while(cubeList[DMM] in cubeList[FBL:FBR+1] or cubeList[DMM] in cubeList[RBL:RBR+1] or 
          cubeList[DMM] in cubeList[BBL:BBR+1] or cubeList[DMM] in cubeList[LBL:LBR+1]):
        for piece in cornerPieces:
            if piece in [FBL, RBL, BBL, LBL] and cubeList[piece] == cubeList[DMM]:
                cubeList, triggerRotations = Cube(''.join(cubeList)).leftTrigger(piece)
                cubeList, topToSideRotations = _rotatePieceFromTopFaceToSideFace(cubeList)
                bottomLayerToTopFaceRotations += triggerRotations + topToSideRotations
            elif piece in [FBR, RBR, BBR, LBR] and cubeList[piece] == cubeList[DMM]:
                cubeList, triggerRotations = Cube(''.join(cubeList)).rightTrigger(piece)
                cubeList, topToSideRotations = _rotatePieceFromTopFaceToSideFace(cubeList)
                bottomLayerToTopFaceRotations += triggerRotations + topToSideRotations
    return cubeList, bottomLayerToTopFaceRotations


    