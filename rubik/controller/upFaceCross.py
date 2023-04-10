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
    if neighboursFound:
        cubeString, rotations = _alignTopNeighbors(cubeString, firstNeighbor, secondNeighbor)
        cubeString, CrossRotations = _performCrossRotations(cubeString)
        rotationsForNeighbors = rotations + CrossRotations
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

def _performCrossRotations(cubeString):
    topCrossRotations = 'FURurf'
    cubeString = Cube(cubeString).rotate(topCrossRotations)
    return cubeString, topCrossRotations

