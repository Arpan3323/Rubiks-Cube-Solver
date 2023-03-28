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
            #requiredTopEdge = edgePair[1]
            pairFound = True
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
    if requiredSideEdge == FTM:
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
    return rotations, requiredTopEdgeLocation

def topEdgeAlignmentRotations(requiredTopEdge, cubeList):
    if requiredTopEdge == UBM:
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
    return rotation 

def _checkMiddleLayerForFlippedEdgePair(cubeList):
    EdgePairsForSideCenters = [(FML, LMR), (RML, FMR), (BML, RMR), (LML, BMR)]
    for edgePair in EdgePairsForSideCenters:
        if cubeList[FMM] != cubeList[edgePair[0]] and cubeList[FMM] == cubeList[edgePair[1]]:
            cubeList, rotations = Cube(cubeList).leftTrigger(edgePair[0])
        elif cubeList[RMM] != cubeList[edgePair[0]] and cubeList[RMM] == cubeList[edgePair[1]]:
            cubeList, rotations = Cube(cubeList).leftTrigger(edgePair[0])
        elif cubeList[BMM] != cubeList[edgePair[0]] and cubeList[BMM] == cubeList[edgePair[1]]:
            cubeList, rotations = Cube(cubeList).leftTrigger(edgePair[0])
        elif cubeList[LMM] != cubeList[edgePair[0]] and cubeList[LMM] == cubeList[edgePair[1]]:
            cubeList, rotations = Cube(cubeList).leftTrigger(edgePair[0])
    return ''.join(cubeList), rotations


