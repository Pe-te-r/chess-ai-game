import pygame
from Game import Game
from Piece import Pawn
from constant import BLACK_MARK


class Main:

    """ This is the main class that is incharge of the game handling """
    def __init__(self):
        self.game_running=True
        self.game=Game()
        self.screen=self.game.screen
        self.valid_moves_position=[]
        

    def mark_squares(self):
        if len(self.valid_moves_position) >0:
            for move in self.valid_moves_position:
                center_y = move[0]* 100 + 100 // 2
                center_x = move[1] * 100 + 100 // 2
                radius = min(100 // 2 - 30, 40)  
                pygame.draw.circle(self.screen, BLACK_MARK, (center_x, center_y), radius)

    def unmark_squares(self):
        for pos in self.valid_moves_position:
            square=self.game.squares[pos[1]][pos[0]]
            square.declare_empty()
    
    def handle_click(self,x,y):
        if self.game.selecte_square == None:
            self.game.selecte_square=self.game.squares[x][y]
        square=self.game.selecte_square
        
        print(x,y)
        if self.game.piece_selected:
            # print(self.valid_moves_position)
            if (y,x) in self.valid_moves_position:
                print('move')
                square_to=self.game.squares[x][y]
                piece=square.piece
                self.unmark_squares()
                square_to.add_piece(piece)
                square.declare_empty()
                self.game.selecte_square=None
                self.valid_moves_position=[]
            else:
                clicked_square=self.game.squares[y][x]
                print(clicked_square.is_empty())
                if clicked_square.is_empty():
                    print('empty_click from move')
                    self.unmark_squares() 
                    self.valid_moves_position=[]
                    print('m')
                else:
                    print('new click no moe')
                    self.unmark_squares()
                    self.valid_moves_position=[]
                    self.game.piece_selected=False
        print(square.is_empty())

        if  not square.is_empty():
            print('click')
            movable_squares=square.piece.valid_moves(y,x)
            valid_position = [(y, x) for y, x in movable_squares  if 0 <= y <= 7 and 0 <= x < 8]
            print(valid_position)
            for position in valid_position:
                next_square=self.game.squares[position[1]][position[0]]
                if next_square.is_empty():
                    self.valid_moves_position.append(position)
                    self.game.piece_selected=True
            valid_position=[]
            self.mark_squares()
        


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

            

            pygame.display.flip()



main=Main()
main.main_loop()
