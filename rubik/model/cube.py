from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self.cube = encodedCube
        
    def rotate(self, directions):
        pass
    
    def get(self):
        return self.cube
        