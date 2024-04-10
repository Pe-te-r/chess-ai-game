import os.path as path
from pygame import image

class Piece:

    '''Please enter a Doc String...'''
    def __init__(self,color,name,value):
        self.color=color
        self.name=name
        self.value=value
        self.image=None
        self.add_image()
        self.adjust_value()
    
    def adjust_value(self):
        if self.color == 'white':
            self.value *= 1
        else:
            self.value *= -1


    def add_image(self):
        self.full_path ='/home/phantom/coding/python-code/python game/chess-ai-game/assets/imgs-80px'
        self.image=image.load(path.join(self.full_path,f'{self.color}_{self.name}.png'))

# class Pawn(Piece):
#     def __init__(self,color,name='pawn',value=1):
#         super().__init__(color,name,value)

#     def valid_moves(self,row,col,squars):
#         valid_squares=[]
#         if self.color=='white':
#             if col==1:
#                 valid_squares=[(row,col+1),(row,col+2)]
#             else:
#                 valid_squares=[(row,col+1)]
#             return valid_squares 
#         else:
#             if col==6:
#                 valid_squares=[(row,col-1),(row,col-2)]
#             else:    
#                 valid_squares=[(row,col-1)]
#             return valid_squares

class Pawn(Piece):
    def __init__(self, color, name='pawn', value=1):
        super().__init__(color, name, value)

    def valid_moves(self, row, col, squares):
        valid_squares = []

        # Define the direction of movement based on the pawn's color
        direction = 1 if self.color == 'white' else -1

        # Check if the square in front of the pawn is empty
        if squares[row][col + direction].is_empty():
            valid_squares.append((row, col + direction))

            # Check for the initial double move
            if (col == 1 and self.color == 'white') or (col == 6 and self.color == 'black'):
                if squares[row][col + 2 * direction].is_empty():
                    valid_squares.append((row, col + 2 * direction))

        # Check for capturing diagonally
        for dcol in [-1, 1]:
            if 0 <= row + dcol < 8:
                target_square = squares[row + dcol][col + direction]
                if not target_square.is_empty() and target_square.piece.color != self.color:
                    valid_squares.append((row + dcol, col + direction))

        return valid_squares

        


class Knight(Piece):
    def __init__(self,color,name='knight',value=4):
        super().__init__(color,name,value)

    def valid_moves(self,row,col,squares):
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
    def __init__(self, color, name='bishop', value=3):
        super().__init__(color, name, value)

    def valid_moves(self, row,col, squares):
        moves=[]
        deltas = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dr, dc in deltas:
            r,c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                square = squares[r][c]
                if square.is_empty() or square.piece.color != self.color:
                    moves.append((r, c))
                    if not square.is_empty():
                        break
                else:
                    break
                r += dr
                c += dc
        
        return moves

class Queen(Piece):
    def __init__(self, color, name='queen', value=8):
        super().__init__(color, name, value)
    
    def valid_moves(self, row, col, squares):
        valid_moves = []

        # Check moves in the same row
        for i in range(1, 8):
            if row + i < 8:
                square = squares[row + i][col]
                if square.is_empty():
                    valid_moves.append((row + i, col))
                elif square.piece.color != self.color:
                    valid_moves.append((row + i, col))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if row - i >= 0:
                square = squares[row - i][col]
                if square.is_empty():
                    valid_moves.append((row - i, col))
                elif square.piece.color != self.color:
                    valid_moves.append((row - i, col))
                    break
                else:
                    break
            else:
                break

        # Check moves in the same column
        for i in range(1, 8):
            if col + i < 8:
                square = squares[row][col + i]
                if square.is_empty():
                    valid_moves.append((row, col + i))
                elif square.piece.color != self.color:
                    valid_moves.append((row, col + i))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if col - i >= 0:
                square = squares[row][col - i]
                if square.is_empty():
                    valid_moves.append((row, col - i))
                elif square.piece.color != self.color:
                    valid_moves.append((row, col - i))
                    break
                else:
                    break
            else:
                break

        # Generate bishop moves (diagonal)
        deltas = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dr, dc in deltas:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                square = squares[r][c]
                if square.is_empty() or square.piece.color != self.color:
                    valid_moves.append((r, c))
                    if not square.is_empty():
                        break
                else:
                    break
                r += dr
                c += dc

        return valid_moves

class Castle(Piece):
    def __init__(self, color, name='rook', value=5):
        super().__init__(color, name, value)

    def valid_moves(self, row, col, squares):
        valid_moves = []

        # Check moves in the same row
        for i in range(1, 8):
            if row + i < 8:
                square = squares[row + i][col]
                if square.is_empty():
                    valid_moves.append((row + i, col))
                elif square.piece.color != self.color:
                    valid_moves.append((row + i, col))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if row - i >= 0:
                square = squares[row - i][col]
                if square.is_empty():
                    valid_moves.append((row - i, col))
                elif square.piece.color != self.color:
                    valid_moves.append((row - i, col))
                    break
                else:
                    break
            else:
                break

        # Check moves in the same column
        for i in range(1, 8):
            if col + i < 8:
                square = squares[row][col + i]
                if square.is_empty():
                    valid_moves.append((row, col + i))
                elif square.piece.color != self.color:
                    valid_moves.append((row, col + i))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if col - i >= 0:
                square = squares[row][col - i]
                if square.is_empty():
                    valid_moves.append((row, col - i))
                elif square.piece.color != self.color:
                    valid_moves.append((row, col - i))
                    break
                else:
                    break
            else:
                break

        return valid_moves



class King(Piece):
    def __init__(self,color,name='king',value=10):
        super().__init__(color,name,value)

    def valid_moves(self,row,col,squares):
        valid_moves=[(row+1,col),(row-1,col),(row,col+1),(row,col-1),(row-1,col-1),(row+1,col+1),(row+1,col-1),(row-1,col+1)]
        # opponent_king_positions = self.get_opponent_king_positions(row, col, squares)
        filtered_moves = []
        for move in valid_moves:
            r, c = move
            if 0 <= r < 8 and 0 <= c < 8:
                check_square=squares[move[0]][move[1]]
                if check_square.is_empty():
                    filtered_moves.append(move)
        return filtered_moves

    def get_opponent_king_positions(self, row, col, squares):
        opponent_king_positions = []
        for i in range(max(0, row - 1), min(8, row + 2)):
            for j in range(max(0, col - 1), min(8, col + 2)):
                if not (i == row and j == col):  # Exclude the king's own square
                    square = squares[i][j]
                    if not square.is_empty() and square.piece.color != self.color and square.piece.name == 'king':
                        opponent_king_positions.append((i, j))
        return opponent_king_positions