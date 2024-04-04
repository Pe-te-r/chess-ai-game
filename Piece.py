import os.path as path
from pygame import image

class Piece:
    def __init__(self,color,name,value):
        self.color=color
        self.name=name
        self.value=value
        self.image=None
        self.add_image()

    def add_image(self):
        self.full_path ='/home/phantom/coding/python-code/python game/chess-ai-game/assets/imgs-80px'
        self.image=image.load(path.join(self.full_path,f'{self.color}_{self.name}.png'))

class Pawn(Piece):
    def __init__(self,color,name='pawn',value=1):
        super().__init__(color,name,value)

    def valid_moves(self,row,col):
        if self.color=='white':
            valid_squares=[(row+1,col)]
            return valid_squares
        else:
            valid_squares=[(row-1,col)]
            return valid_squares
        
        


class Knight(Piece):
    def __init__(self,color,name='knight',value=4):
        super().__init__(color,name,value)

    def valid_moves(self,row,col):
        valid_squares=[
            (row+1,col+2),
            (row+2,col+1),
            (row-1,col-2),
            (row-2,col-1),
            (row+1,col-2),
            (row+2,col-1),
            (row-1,col+2),
            (row-2,col+1)
            ]
        return valid_squares

class Bishop(Piece):
    def __init__(self,color,name='bishop',value=3):
        super().__init__(color,name,value)

    def valid_moves(self):
        pass

class Queen(Piece):
    def __init__(self,color,name='queen',value=8):
        super().__init__(color,name,value)
    
    def valid_moves(self):
        pass

class Castle(Piece):
    def __init__(self,color,name='rook',value=5):
        super().__init__(color,name,value)

    def valid_moves(self):
        pass

class King(Piece):
    def __init__(self,color,name='king',value=10):
        super().__init__(color,name,value)

    def valid_moves(self):
        pass

    
