import pygame
from Game import Game
from Piece import Pawn
from constant import BLACK_MARK,RED_MARK,WHITE_MARK
from copy import deepcopy

class Main:

    """ This is the main class that is incharge of the game handling """
    def __init__(self):
        self.game_running=True
        self.game=Game()
        self.screen=self.game.screen
        self.valid_moves_position=[]
        self.capture_postion=[]

    def mark_squares(self):
        if len(self.valid_moves_position) >0:
            for square in self.valid_moves_position:
                center_x=100//2
                center_y=100//2
                radius = min(100 // 2 - 30, 40)
                if self.game.selected_piece.color =='black':
                    pygame.draw.circle(square.surface, BLACK_MARK, (center_x, center_y), radius)
                else:
                    pygame.draw.circle(square.surface,WHITE_MARK,(center_x,center_y),radius)
                square.show_square()

        if len(self.capture_postion)>0:
            for square in self.capture_postion:
                center_x=100//2
                center_y=100//2
                radius=min(100//2-30,40)
                pygame.draw.circle(square.surface,RED_MARK,(center_x,center_y),radius)
                square.show_square()


    def unmark_squares(self):
        for square in self.valid_moves_position:
            square.declare_empty()
        
        for square in self.capture_postion:
            piece=square.piece
            square.declare_empty()
            square.add_piece(piece)
        self.capture_postion=[]
    

    def handle_marking(self,x,y):
        self.game.selected_piece=self.game.selected_square.piece
        valid_moves=self.game.selected_piece.valid_moves(x,y,self.game.squares)
        valid_moves=[(y,x)for x,y in valid_moves if 0<= x<=7 and 0<=y<8]
        print(valid_moves)
        if len(valid_moves)>0:
            for position in valid_moves:
                next_square_mark=self.game.squares[position[1]][position[0]]
                if next_square_mark.is_empty():
                    self.valid_moves_position.append(next_square_mark)
                else:
                    value=next_square_mark.value
                    # if (self.game.selected_square.value>0 and value <0)or(self.game.selected_square.value<0 and value >0):
                    if (self.game.selected_piece.color != next_square_mark.piece.color):
                        self.capture_postion.append(next_square_mark)
        else:
            self.clear_cache()

        if len(self.valid_moves_position)>0:
            self.game.piece_selected=True
        self.mark_squares()

    def handle_movement(self,x,y):
        square_to=self.game.squares[x][y]
        piece=self.game.selected_piece
        self.unmark_squares()
        square_to.add_piece(piece)
        self.game.selected_square.declare_empty()
        self.piece_selected=False
        self.game.selected_square=None
        self.game.selected_piece=None
        self.valid_moves_position=[]
        
    def clear_cache(self):
        self.unmark_squares()
        self.game.selected_piece=None
        self.game.selected_square=None
        self.valid_moves_position=[]
        self.piece_selected=False
    
    def capture_piece(self,x,y):
        square_piece_captured=self.game.squares[x][y]
        square_piece_captured.declare_empty()
        square_piece_captured.add_piece(self.game.selected_piece)

    def handle_click(self,x,y):
        if self.game.selected_square==None:
            self.game.selected_square=self.game.squares[x][y]
        
        if self.game.piece_selected:
            if self.game.squares[x][y] in self.valid_moves_position:
                self.handle_movement(x,y)
            elif self.game.squares[x][y].is_empty():
                # print('m')
                self.clear_cache()
            elif self.game.squares[x][y] in self.capture_postion:
                # print('m')
                self.capture_piece(x,y)
                self.game.selected_square.declare_empty()
                self.clear_cache()
            else:
                if not self.game.squares[x][y].is_empty():
                    print('another')
                    self.unmark_squares()
                    # self.clear_cache()
                    self.capture_postion=[]
                    self.valid_moves_position=[]
                    self.game.selected_square=self.game.squares[x][y]
                    self.game.selected_piece=self.game.selected_square.piece
        if self.game.selected_square != None:
            if not self.game.selected_square.is_empty():
                self.handle_marking(x,y)

    def main_loop(self):
        game=self.game
        game.show_background()
        
        game.add_image()
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running=False
            
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    mouse_x=pos[0]//100
                    mouse_y=pos[1]//100
                    self.handle_click(mouse_x,mouse_y)
                    print(self.game.selected_piece)
            pygame.display.flip()



main=Main()
main.main_loop()
