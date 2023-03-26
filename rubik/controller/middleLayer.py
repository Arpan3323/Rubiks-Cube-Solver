from rubik.model.constants import *
from rubik.model.cube import Cube
import rubik.controller.bottomLayer as bl

def solveMiddleLayer(theCube: Cube) -> str:

    cubeList = theCube.get()

    if verifyMiddleLayerExists(cubeList):
        return [cubeList, '']
    
    if bl.verifyBottomLayerExists(cubeList) == False:
        cubeList = _alignToBottomLayer(theCube)
    
    return 'B'      #TODO:  remove this stubbed value

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
    sideAndTopEdgePairs = [(FTM, UBM), (RTM, UMR), (BTM, UTM), (LTM, UML)]
    pairFound = False
    for edgePair in sideAndTopEdgePairs:
        if cubeList[edgePair[0]] != cubeList[UMM] and cubeList[edgePair[1]] != cubeList[UMM] and not pairFound:
            requiredSideEdge = edgePair[0]
            #requiredTopEdge = edgePair[1]
            pairFound = True
    if cubeList[requiredSideEdge] != cubeList[FMM]:
        sideEdgeToCenterRotations, requiredTopEdge = sideEdgeAlignmentRotations(requiredSideEdge, cubeList)
    cubeList = Cube(cubeList).rotate(sideEdgeToCenterRotations)
    return cubeList, sideEdgeToCenterRotations


def sideEdgeAlignmentRotations(requiredSideEdge, cubeList):
    if cubeList[requiredSideEdge] == cubeList[RMM]:
        rotations = 'UUU'
        requiredTopEdgeLocation = UMR
    elif cubeList[requiredSideEdge] == cubeList[BMM]:
        rotations = 'UU'
        requiredTopEdgeLocation = UTM
    elif cubeList[requiredSideEdge] == cubeList[LMM]:
        rotations = 'U'
        requiredTopEdgeLocation = UML
    return rotations, requiredTopEdgeLocation
