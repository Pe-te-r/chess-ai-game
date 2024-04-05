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

    def valid_moves(self,col,row):
        valid_moves=[]
        diagonals = [
        (1, 1),  # Top-right diagonal (m=1, c=1)
        (-1, 1),  # Top-left diagonal (m=-1, c=1)
        (1, -1),  # Bottom-right diagonal (m=1, c=-1)
        (-1, -1)  # Bottom-left diagonal (m=-1, c=-1)
    ]

        for dr, dc in diagonals:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                valid_moves.append((c, r))
                r += dr
                c += dc
        

        return valid_moves

class Queen(Piece):
    def __init__(self,color,name='queen',value=8):
        super().__init__(color,name,value)
    
    def valid_moves(self,row,col):
        moves = []

    # Generate rook moves (horizontal and vertical)
        for i in range(8):
            if i != col:
                moves.append((row, i))  # Horizontal moves
            if i != row:
                moves.append((i, col))  # Vertical moves

        # Generate bishop moves (diagonal)
        deltas = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dr, dc in deltas:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                moves.append((r, c))
                r += dr
                c += dc

        return moves

class Castle(Piece):
    def __init__(self,color,name='rook',value=5):
        super().__init__(color,name,value)

    def valid_moves(self,row,col):
        valid_moves=[]
        for i in range(8):
            valid_moves.append((row+i,col))
            valid_moves.append((row,col+i))
            valid_moves.append((row-i,col))
            valid_moves.append((row,col-i))
        
        return valid_moves


class King(Piece):
    def __init__(self,color,name='king',value=10):
        super().__init__(color,name,value)

    def valid_moves(self,row,col):
        valid_moves=[(row+1,col),(row-1,col),(row,col+1),(row,col-1),(row-1,col-1),(row+1,col+1),(row+1,col-1),(row-1,col+1)]
        return valid_moves
    
