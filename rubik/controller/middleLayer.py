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
            rotations += topLayerEdgePairRotations
            
    
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
    return (
        theCube.rotate(bottomLayerRotations)
        if bottomLayerRotations != ''
        else theCube.get()
    )

#checks if any edge pair is in the top layer. If found, captures it and sends it to edgePairFoundInTopLayer
#if not found, calls the component _checkMiddleLayerForFlippedEdgePair to check if any flipped edge pair exists
def _checkTopLayerForEdgePair(cubeList):
    topLayerEdgePairRotations = ''
    sideAndTopEdgePairs = [(FTM, UBM), (RTM, UMR), (BTM, UTM), (LTM, UML)]
    pairFound = False
    for edgePair in sideAndTopEdgePairs:
        if ((cubeList[edgePair[0]] != cubeList[UMM]) and 
            (cubeList[edgePair[1]] != cubeList[UMM] and not pairFound)):
            requiredSideEdge = edgePair[0]
            pairFound = True
    cubeList, returnedRotations = (
        _edgePairFoundInTopLayer(cubeList, topLayerEdgePairRotations, requiredSideEdge)
        if pairFound
        else _checkMiddleLayerForFlippedEdgePair(cubeList)
    )
    topLayerEdgePairRotations += returnedRotations
    return cubeList, topLayerEdgePairRotations

def _edgePairFoundInTopLayer(cubeList, topLayerEdgePairRotations, requiredSideEdge):
    sideEdgeToCenterRotations, requiredTopEdge = _sideEdgeAlignmentRotations(requiredSideEdge, cubeList)
    if sideEdgeToCenterRotations != '':
        topLayerEdgePairRotations += sideEdgeToCenterRotations
        cubeList = Cube(cubeList).rotate(sideEdgeToCenterRotations)
    topEdgeRotations = _topEdgeAlignmentRotations(requiredTopEdge, cubeList)
    topLayerEdgePairRotations += topEdgeRotations
    cubeList = Cube(cubeList).rotate(topEdgeRotations)
    alignBottomLayer = bl.solveBottomLayer(Cube(cubeList))[1]
    cubeList = Cube(cubeList).rotate(alignBottomLayer)
    topLayerEdgePairRotations += alignBottomLayer
    return cubeList, topLayerEdgePairRotations


def _sideEdgeAlignmentRotations(requiredSideEdge, cubeList):
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
    
def _topEdgeAlignmentRotations(requiredTopEdge, cubeList):
    rotationsToReturn = ''
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
            rotationsToReturn = rotation
    return rotationsToReturn
        
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
    cubeList, bottomLayerRotations = bl.solveBottomLayer(Cube(''.join(cubeList)))
    middleLayerFlippedEdgeRotations += rotations + bottomLayerRotations
    return ''.join(cubeList), middleLayerFlippedEdgeRotations


