from rubik.model.constants import *
from rubik.model.cube import Cube
import rubik.controller.bottomLayer as bl

def solveMiddleLayer(theCube: Cube) -> str:

    cubeList = theCube.get()
    rotations = ''

    if verifyMiddleLayerExists(cubeList):
        return [cubeList, '']
    
    if bl.verifyBottomLayerExists(cubeList) == False:
        cubeList = _alignToBottomLayer(theCube)
    
    if verifyMiddleLayerExists(cubeList) == False:
        while(verifyMiddleLayerExists(cubeList) == False):
            cubeList, topLayerEdgePairRotations = _checkTopLayerForEdgePair(cubeList)
            #cubeList, middleLayerRotations = _rotateMiddleLayerEdgePairToBottom(cubeList)
            rotations += topLayerEdgePairRotations #+ middleLayerRotations
            
    
    return cubeList, rotations

def verifyMiddleLayerExists(cubeList):
    return(bl.verifyBottomLayerExists(cubeList) 
           and cubeList[FMM] == cubeList[FML]
           and cubeList[FMM] == cubeList[FMR]
           and cubeList[RMM] == cubeList[RML]
           and cubeList[RMM] == cubeList[RMR]
           and cubeList[BMM] == cubeList[BML]
           and cubeList[BMM] == cubeList[BMR]
           and cubeList[LMM] == cubeList[LML]
           and cubeList[LMM] == cubeList[LMR])

def _alignToBottomLayer(theCube):
    bottomLayerRotations = bl.solveBottomLayer(theCube)[1]
    return theCube.rotate(bottomLayerRotations)

def _checkTopLayerForEdgePair(cubeList):
    topLayerEdgePairRotations = ''
    sideAndTopEdgePairs = [(FTM, UBM), (RTM, UMR), (BTM, UTM), (LTM, UML)]
    pairFound = False
    for edgePair in sideAndTopEdgePairs:
        if cubeList[edgePair[0]] != cubeList[UMM] and cubeList[edgePair[1]] != cubeList[UMM] and not pairFound:
            requiredSideEdge = edgePair[0]
            pairFound = True
    cubeList, returnedRotations = (
        edgePairFoundInTopLayer(cubeList, topLayerEdgePairRotations, requiredSideEdge)
        if pairFound
        else _checkMiddleLayerForFlippedEdgePair(cubeList)
    )
    topLayerEdgePairRotations += returnedRotations
    return cubeList, topLayerEdgePairRotations

def edgePairFoundInTopLayer(cubeList, topLayerEdgePairRotations, requiredSideEdge):
    sideEdgeToCenterRotations, requiredTopEdge = sideEdgeAlignmentRotations(requiredSideEdge, cubeList)
    if sideEdgeToCenterRotations != '':
        topLayerEdgePairRotations += sideEdgeToCenterRotations
        cubeList = Cube(cubeList).rotate(sideEdgeToCenterRotations)
    topEdgeRotations = topEdgeAlignmentRotations(requiredTopEdge, cubeList)
    topLayerEdgePairRotations += topEdgeRotations
    cubeList = Cube(cubeList).rotate(topEdgeRotations)
    alignBottomLayer = bl.solveBottomLayer(Cube(cubeList))[1]
    cubeList = Cube(cubeList).rotate(alignBottomLayer)
    topLayerEdgePairRotations += alignBottomLayer
    return cubeList, topLayerEdgePairRotations


def sideEdgeAlignmentRotations(requiredSideEdge, cubeList):
    rotationsAndTopEdgeLocation = {
        (FTM, FMM): ('', UBM),
        (FTM, RMM): ('UUU', UMR),
        (FTM, BMM): ('UU', UTM),
        (FTM, LMM): ('U', UML),
        (RTM, RMM): ('', UMR),
        (RTM, BMM): ('UUU', UTM),
        (RTM, LMM): ('UU', UML),
        (RTM, FMM): ('U', UBM),
        (BTM, BMM): ('', UTM),
        (BTM, LMM): ('UUU', UML),
        (BTM, FMM): ('UU', UBM),
        (BTM, RMM): ('U', UMR),
        (LTM, LMM): ('', UML),
        (LTM, FMM): ('UUU', UBM),
        (LTM, RMM): ('UU', UMR),
        (LTM, BMM): ('U', UTM),
    }
    for edgeAndCenter, (rotations, requiredTopEdgeLocation) in rotationsAndTopEdgeLocation.items():
        if cubeList[edgeAndCenter[0]] == cubeList[edgeAndCenter[1]] and edgeAndCenter[0] == requiredSideEdge:
            return rotations, requiredTopEdgeLocation
    '''if requiredSideEdge == FTM:
        if cubeList[requiredSideEdge] == cubeList[FMM]:
            rotations = ''
            requiredTopEdgeLocation = UBM
        if cubeList[requiredSideEdge] == cubeList[RMM]:
            rotations = 'UUU'
            requiredTopEdgeLocation = UMR
        elif cubeList[requiredSideEdge] == cubeList[BMM]:
            rotations = 'UU'
            requiredTopEdgeLocation = UTM
        elif cubeList[requiredSideEdge] == cubeList[LMM]:
            rotations = 'U'
            requiredTopEdgeLocation = UML
    if requiredSideEdge == RTM:
        if cubeList[requiredSideEdge] == cubeList[RMM]:
            rotations = ''
            requiredTopEdgeLocation = UMR
        elif cubeList[requiredSideEdge] == cubeList[BMM]:
            rotations = 'UUU'
            requiredTopEdgeLocation = UTM
        elif cubeList[requiredSideEdge] == cubeList[LMM]:
            rotations = 'UU'
            requiredTopEdgeLocation = UML
        elif cubeList[requiredSideEdge] == cubeList[FMM]:
            rotations = 'U'
            requiredTopEdgeLocation = UBM
    if requiredSideEdge == BTM:
        if cubeList[requiredSideEdge] == cubeList[BMM]:
            rotations = ''
            requiredTopEdgeLocation = UTM
        elif cubeList[requiredSideEdge] == cubeList[LMM]:
            rotations = 'UUU'
            requiredTopEdgeLocation = UML
        elif cubeList[requiredSideEdge] == cubeList[FMM]:
            rotations = 'UU'
            requiredTopEdgeLocation = UBM
        elif cubeList[requiredSideEdge] == cubeList[RMM]:
            rotations = 'U'
            requiredTopEdgeLocation = UMR
    if requiredSideEdge == LTM:
        if cubeList[requiredSideEdge] == cubeList[LMM]:
            rotations = ''
            requiredTopEdgeLocation = UML
        elif cubeList[requiredSideEdge] == cubeList[FMM]:
            rotations = 'UUU'
            requiredTopEdgeLocation = UBM
        elif cubeList[requiredSideEdge] == cubeList[RMM]:
            rotations = 'UU'
            requiredTopEdgeLocation = UMR
        elif cubeList[requiredSideEdge] == cubeList[BMM]:
            rotations = 'U'
            requiredTopEdgeLocation = UTM
    return rotations, requiredTopEdgeLocation'''

def topEdgeAlignmentRotations(requiredTopEdge, cubeList):
    matchingTopEdgeAndCenter = {
        (UBM, LMM): f'u{Cube(cubeList).leftTrigger(requiredTopEdge)[1]}',
        (UBM, RMM): f'U{Cube(cubeList).rightTrigger(requiredTopEdge)[1]}',
        (UMR, FMM): f'u{Cube(cubeList).leftTrigger(requiredTopEdge)[1]}',
        (UMR, BMM): f'U{Cube(cubeList).rightTrigger(requiredTopEdge)[1]}',
        (UTM, RMM): f'u{Cube(cubeList).leftTrigger(requiredTopEdge)[1]}',
        (UTM, LMM): f'U{Cube(cubeList).rightTrigger(requiredTopEdge)[1]}',
        (UML, BMM): f'u{Cube(cubeList).leftTrigger(requiredTopEdge)[1]}',
        (UML, FMM): f'U{Cube(cubeList).rightTrigger(requiredTopEdge)[1]}',
    }
    for topEdgeAndCenter, rotation in matchingTopEdgeAndCenter.items():
        if cubeList[topEdgeAndCenter[0]] == cubeList[topEdgeAndCenter[1]] and topEdgeAndCenter[0] == requiredTopEdge:
            return rotation
    '''if requiredTopEdge == UBM:
        if cubeList[requiredTopEdge] == cubeList[LMM]:
            rotation = f'u{Cube(cubeList).leftTrigger(requiredTopEdge)[1]}'
        elif cubeList[requiredTopEdge] == cubeList[RMM]:
            rotation = f'U{Cube(cubeList).rightTrigger(requiredTopEdge)[1]}'
    if requiredTopEdge == UMR:
        if cubeList[requiredTopEdge] == cubeList[FMM]:
            rotation = f'u{Cube(cubeList).leftTrigger(requiredTopEdge)[1]}'
        elif cubeList[requiredTopEdge] == cubeList[BMM]:
            rotation = f'U{Cube(cubeList).rightTrigger(requiredTopEdge)[1]}'
    if requiredTopEdge == UTM:
        if cubeList[requiredTopEdge] == cubeList[RMM]:
            rotation = f'u{Cube(cubeList).leftTrigger(requiredTopEdge)[1]}'
        elif cubeList[requiredTopEdge] == cubeList[LMM]:
            rotation = f'U{Cube(cubeList).rightTrigger(requiredTopEdge)[1]}'
    if requiredTopEdge == UML:
        if cubeList[requiredTopEdge] == cubeList[BMM]:
            rotation = f'u{Cube(cubeList).leftTrigger(requiredTopEdge)[1]}'
        elif cubeList[requiredTopEdge] == cubeList[FMM]:
            rotation = f'U{Cube(cubeList).rightTrigger(requiredTopEdge)[1]}'
    return rotation''' 

def _checkMiddleLayerForFlippedEdgePair(cubeList):
    middleLayerFlippedEdgeRotations = ''
    rotations = ''
    flippedEdgeAndCenter = {
        (FMM, FML): Cube(cubeList).leftTrigger(FML),
        (FMM, FMR): Cube(cubeList).rightTrigger(FMR),
        (RMM, RML): Cube(cubeList).leftTrigger(RML),
        (RMM, RMR): Cube(cubeList).rightTrigger(RMR),
        (BMM, BML): Cube(cubeList).leftTrigger(BML),
        (BMM, BMR): Cube(cubeList).rightTrigger(BMR),
        (LMM, LML): Cube(cubeList).leftTrigger(LML),
        (LMM, LMR): Cube(cubeList).rightTrigger(LMR),
    }
    flippedEdgeTriggered = False
    for edgeAndCenter, cubeListAndRotation in flippedEdgeAndCenter.items():
        if cubeList[edgeAndCenter[0]] != cubeList[edgeAndCenter[1]] and not flippedEdgeTriggered:
            cubeList, rotations = cubeListAndRotation
            flippedEdgeTriggered = True
    '''if cubeList[FMM] != cubeList[FML]:
        cubeList, rotations = Cube(cubeList).leftTrigger(FML)
    elif cubeList[FMM] != cubeList[FMR]:
        cubeList, rotations = Cube(cubeList).rightTrigger(FMR)
    elif cubeList[RMM] != cubeList[RML]:
        cubeList, rotations = Cube(cubeList).leftTrigger(RML)
    elif cubeList[RMM] != cubeList[RMR]:
        cubeList, rotations = Cube(cubeList).rightTrigger(RMR)
    elif cubeList[BMM] != cubeList[BML]:
        cubeList, rotations = Cube(cubeList).leftTrigger(BML)
    elif cubeList[BMM] != cubeList[BMR]:
        cubeList, rotations = Cube(cubeList).rightTrigger(BMR)
    elif cubeList[LMM] != cubeList[LML]:
        cubeList, rotations = Cube(cubeList).leftTrigger(LML)
    elif cubeList[LMM] != cubeList[LMR]:
        cubeList, rotations = Cube(cubeList).rightTrigger(LMR)'''
    cubeList, bottomLayerRotations = bl.solveBottomLayer(Cube(''.join(cubeList)))
    middleLayerFlippedEdgeRotations += rotations + bottomLayerRotations
    return ''.join(cubeList), middleLayerFlippedEdgeRotations


