import pygame
from constant import *
from Square import Square
from Piece import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess game for trial')
        self.squares=[]
        self.piece_selected=False
        self.selected_square=None
        # self.original_square=None
        self.show_background()
        self.selected_piece=None
    def show_background(self):

        for row in range(8):
            row_array=[]
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BLACK # Black for even sum, space for odd
                square=Square(row,col,color)
                square.set_main_screen(self.screen)
                square.show_square()
                row_array.append(square)
            self.squares.append(row_array)

    def add_image(self):
        for row in range(8):
            for col in range(8):
                square=self.squares[col][row]
                if row==1:
                    square.add_piece(Pawn('white'))
                if row==6:
                    square.add_piece(Pawn('black'))
                if (col == 0 or col ==7) and row ==0:
                    square.add_piece(Castle('white'))
                if (col==0 or col == 7) and row == 7:
                    square.add_piece(Castle('black'))
                if (col==1 or col == 6) and row ==0:
                    square.add_piece(Knight('white'))
                if (col==1 or col ==6 ) and row == 7:
                    square.add_piece(Knight('black'))
                if (col==2 or col ==5) and row == 0:
                    square.add_piece(Bishop('white'))
                if (col==2 or col ==5) and row ==7:
                    square.add_piece(Bishop('black'))
                if col==4 and row ==0:
                    square.add_piece(Queen('white'))
                if col ==4 and row == 7:
                    square.add_piece(Queen('black'))
                if col ==3 and row ==0:
                    square.add_piece(King('white'))
                if col ==3 and row ==7:
                    square.add_piece(King('black'))
