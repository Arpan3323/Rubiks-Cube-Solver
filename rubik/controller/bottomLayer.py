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
    rotationsIfAPieceIsLeftOnTop = ''
     
    if _verifyBottomLayerExists(cubeList) == False:
        cubeList, TopLayerToBottomrotations = rotateTopLayerPieceToBottom(cubeList)
        cubeList, topFaceToSideRotations = rotatePieceFromTopFaceToSideFace(cubeList)
        cubeList, bottomLayerRotations = rotateBottomLayerPieceToTopFace(cubeList)
        while cubeList[DMM] in cubeList[UTL:UTR+1] or cubeList[DMM] in cubeList[UBL:UBR+1]:
            cubeList, rotationsIfAPieceIsLeftOnTop = rotatePieceFromTopFaceToSideFace(cubeList)
        rotations += TopLayerToBottomrotations + topFaceToSideRotations + bottomLayerRotations + rotationsIfAPieceIsLeftOnTop
       
    
    return cubeList, rotations

def _verifyBottomLayerExists(cubeList):
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

def alignToBottomCross(theCube):
    bottomCrossRotations = bc.solveBottomCross(theCube)
    return list(theCube.get())

def rotatePieceFromTopFaceToSideFace(cubeList):
    # DownFaceCorners = [DBL, DBR, DTL, DTR]
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
                    cornerToRotate, downFaceCorner = stackedCornerLocation(downFaceCorner, cornerToRotate)
                    rotationsBeforeTrigger += 'U'
                    cubeList = Cube(''.join(cubeList)).rotate('U')
                cubeList, returnedRotations = Cube(''.join(cubeList)).rightTrigger(cornerToRotate)
                rotationsAfterTrigger += returnedRotations
                topToSideRotations += rotationsBeforeTrigger + rotationsAfterTrigger
    cubeList, topLayerRotations = rotateTopLayerPieceToBottom(cubeList)
    topToSideRotations += topLayerRotations

    return cubeList, topToSideRotations

def stackedCornerLocation(downFaceCorner, cornerToRotate):
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

def rotateTopLayerPieceToBottom(cubeList):
    TopLayerPieceToBottomRotations = ''

    while ((cubeList[DMM] in cubeList[FTL:FTR+1]) 
           or (cubeList[DMM] in cubeList[RTL:RTR+1]) 
           or (cubeList[DMM] in cubeList[BTL:BTR+1]) 
           or (cubeList[DMM] in cubeList[LTL:LTR+1])):
        cubeList, returnedRotations, triggerPieceLocation = alignTopLayerPieceWithCenter(cubeList)
        TopLayerPieceToBottomRotations += returnedRotations

        if triggerPieceLocation in [FTL, RTL, BTL, LTL]:
            cubeList, returnedRotations = Cube(''.join(cubeList)).leftTrigger(triggerPieceLocation)
            TopLayerPieceToBottomRotations += returnedRotations

        elif triggerPieceLocation in [FTR, RTR, BTR, LTR]:
            cubeList, returnedRotations = Cube(''.join(cubeList)).rightTrigger(triggerPieceLocation)
            TopLayerPieceToBottomRotations += returnedRotations

    return cubeList, TopLayerPieceToBottomRotations


def alignTopLayerPieceWithCenter(cubeList):
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

    if cubeList[topLayerPieceToAlignWithCenter] == cubeList[FMM]:
        while topLayerPieceToAlignWithCenter not in [FTR, FTL]:
            topLayerPieceToAlignWithCenter = pieceLocationAfterRotation(topLayerPieceToAlignWithCenter)
            cubeList =  list(Cube(''.join(cubeList)).rotate('u'))
            alignTopLayerRotations += 'u'

    elif cubeList[topLayerPieceToAlignWithCenter] == cubeList[RMM]:
        while topLayerPieceToAlignWithCenter not in [RTR, RTL]:
            topLayerPieceToAlignWithCenter = pieceLocationAfterRotation(topLayerPieceToAlignWithCenter)
            cubeList =  list(Cube(''.join(cubeList)).rotate('u'))
            alignTopLayerRotations += 'u'

    elif cubeList[topLayerPieceToAlignWithCenter] == cubeList[BMM]:
        while topLayerPieceToAlignWithCenter not in [BTR, BTL]:
            topLayerPieceToAlignWithCenter = pieceLocationAfterRotation(topLayerPieceToAlignWithCenter)
            cubeList =  list(Cube(''.join(cubeList)).rotate('u'))
            alignTopLayerRotations += 'u'

    elif cubeList[topLayerPieceToAlignWithCenter] == cubeList[LMM]:
        while topLayerPieceToAlignWithCenter not in [LTR, LTL]:
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


def rotateBottomLayerPieceToTopFace(cubeList):

    while(cubeList[DMM] in cubeList[FBL:FBR+1] or cubeList[DMM] in cubeList[RBL:RBR+1] or 
          cubeList[DMM] in cubeList[BBL:BBR+1] or cubeList[DMM] in cubeList[LBL:LBR+1]):
        
        if cubeList[DMM] == cubeList[FBL]:
            cubeList = triggerBottomLayerPiece(cubeList, FBL)[0]

        elif cubeList[DMM] == cubeList[FBR]:
            cubeList = triggerBottomLayerPiece(cubeList, FBR)[0]

        elif cubeList[DMM] == cubeList[RBL]:
            cubeList = triggerBottomLayerPiece(cubeList, RBL)[0]

        elif cubeList[DMM] == cubeList[RBR]:
            cubeList = triggerBottomLayerPiece(cubeList, RBR)[0]

        elif cubeList[DMM] == cubeList[BBL]:
            cubeList = triggerBottomLayerPiece(cubeList, BBL)[0]

        elif cubeList[DMM] == cubeList[BBR]:
            cubeList = triggerBottomLayerPiece(cubeList, BBR)[0]

        elif cubeList[DMM] == cubeList[LBL]:
            cubeList = triggerBottomLayerPiece(cubeList, LBL)[0]

        elif cubeList[DMM] == cubeList[LBR]:
            cubeList = triggerBottomLayerPiece(cubeList, LBR)[0]

        bottomLayerRotations = rotatePieceFromTopFaceToSideFace(cubeList)[1]
    return cubeList, bottomLayerRotations

def triggerBottomLayerPiece(cubeList, pieceLocation):
    #bottomLayerToTopFaceRotations = ''
    if pieceLocation in [FBL, RBL, BBL, LBL]:
        cubeList, triggerRotations = Cube(''.join(cubeList)).leftTrigger(pieceLocation)

    elif pieceLocation in [FBR, RBR, BBR, LBR]:
        cubeList, triggerRotations = Cube(''.join(cubeList)).rightTrigger(pieceLocation)

    cubeList, topToSideRotations = rotatePieceFromTopFaceToSideFace(cubeList)
    bottomLayerToTopFaceRotations += triggerRotations + topToSideRotations
    return cubeList, bottomLayerToTopFaceRotations
