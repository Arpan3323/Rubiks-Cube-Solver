from rubik.model.constants import *
from rubik.model.cube import Cube
import rubik.controller.middleLayer as ml

def solveUpCross(theCube: Cube) -> str:
    cubeString = theCube.get()

    if verifyTopCrossExists(cubeString):
        return [cubeString, '']
    
    if ml.verifyMiddleLayerExists(cubeString) == False:
        cubeString = _alignMiddleLayer(theCube)
      
    return 'L'      #TODO:  remove this stubbed value

def verifyTopCrossExists(cubeString):
    return(ml.verifyMiddleLayerExists(cubeString)
           and cubeString[UBM] == cubeString[UMM]
           and cubeString[UMR] == cubeString[UMM]
           and cubeString[UTM] == cubeString[UMM]
           and cubeString[UML] == cubeString[UMM])

def _alignMiddleLayer(theCube):
    middleLayerRotations = ml.solveMiddleLayer(theCube)[1]
    return theCube.rotate(middleLayerRotations)

def _createTopCross(cubeString):
    cubeString, rotations = _checkTopForNeighbors(cubeString)
    return cubeString, rotations

    

def _checkTopForNeighbors(cubeString):
    topNeighborEdges = [(UBM, UMR, UML), (UMR, UBM, UTM), (UTM, UMR, UML), (UML, UTM, UBM)]
    neighboursFound = False
    for edge in topNeighborEdges:
        if cubeString[edge[0]] == cubeString[UMM]:
            if cubeString[edge[1]] == cubeString[UMM] and not neighboursFound:
                firstNeighbor, secondNeighbor = edge[0], edge[1]
                neighboursFound = True
            elif cubeString[edge[2]] == cubeString[UMM] and not neighboursFound:
                firstNeighbor, secondNeighbor = edge[0], edge[2]
                neighboursFound = True
    rotationsForNeighbors = ''
    if neighboursFound:
        cubeString, rotations = _alignTopNeighbors(cubeString, firstNeighbor, secondNeighbor)
        cubeString, CrossRotations = _performCrossRotations(cubeString)
        rotationsForNeighbors = rotations + CrossRotations
        #return cubeString, rotationsForNeighbors
    else:
        cubeString, rotations = _checkTopForAdjacentEdges(cubeString)
        rotationsForNeighbors = rotations
        #return cubeString, rotations
    return cubeString, rotationsForNeighbors



def _alignTopNeighbors(cubeString, firstNeighbor, secondNeighbor):
    neighborRotations = {
        (UBM, UMR) : 'UU',
        (UBM, UML) : 'U',
        #(UMR, UBM) : 'UU',
        #(UMR, UTM) : 'UUU',
        (UTM, UMR) : 'UUU',
        #(UTM, UML) : '',
        (UML, UTM) : '',
        #(UML, UBM) : 'U',
    }
    for edges in neighborRotations:
        if (firstNeighbor in edges and secondNeighbor in edges):
            rotations = neighborRotations[edges]
    if rotations != '': cubeString = Cube(cubeString).rotate(neighborRotations[edges])
    return cubeString, rotations

def _checkTopForAdjacentEdges(cubeString):
    topAdjacentEdges = [(UBM, UTM), (UMR, UML)]
    adjacentEdgesFound = False
    adjacentEdgeRotations = ''
    for edges in topAdjacentEdges:
        if (cubeString[edges[0]] == cubeString[UMM] and cubeString[edges[1]] == cubeString[UMM] 
            and not adjacentEdgesFound):
            adjacentEdgesFound = True
            firstEdge, secondEdge = edges[0], edges[1]
    if adjacentEdgesFound:
        if firstEdge == UMR:
            cubeString = Cube(cubeString).rotate('U')
            adjacentEdgeRotations += 'U'
        cubeString, crossRotations = _performCrossRotations(cubeString)
        cubeString, rotations = _checkTopForNeighbors(cubeString)
        adjacentEdgeRotations += crossRotations + rotations
        return cubeString, adjacentEdgeRotations
    else:
        cubeString, crossRotations = _performCrossRotations(cubeString)
        cubeString, rotations = _checkTopForAdjacentEdges(cubeString)
        adjacentEdgeRotations += crossRotations + rotations
        return cubeString, adjacentEdgeRotations
    


        

def _performCrossRotations(cubeString):
    topCrossRotations = 'FURurf'
    cubeString = Cube(cubeString).rotate(topCrossRotations)
    return cubeString, topCrossRotations

