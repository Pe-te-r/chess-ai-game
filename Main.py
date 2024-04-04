import pygame
from Game import Game


class Main:

    """ This is the main class that is incharge of the game handling """
    def __init__(self):
        self.game_running=True
        self.game=Game()
        self.screen=self.game.screen

    def mark_piece(self,row,col):
        position=piece.valid_moves(row,col)
        center_y = pos_x* 100 + 100 // 2
        center_x = pos_y * 100 + 100 // 2
        radius = min(100 // 2 - 30, 40)  
        self.valid_moves.append(square)
        draw.circle(self.screen, BLACK_MARK, (center_x, center_y), radius)

    
    
    def handle_click(self,x,y):
        square=self.game.squares[x][y]
        
        if not square.is_empty():
            valid_positions=[]
            movable_squares=square.piece.valid_moves(y,x)

            valid_position = [(y, x) for y, x in movable_squares  if 0 <= y <= 7 and 0 <= x < 8]
            
            print(valid_position)

            for square in self.game.squares:
                for i in square:
                    print(i.value)

            # for position in valid_position:
            
                # next_square=self.game.squares[position[0]][position[1]]

                # print(next_square.is_empty())
                # if next_square.is_empty():
                    # valid_positions.append(position)
        
                # print(valid_positions)
        

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
