import pygame
from constant import *
from Square import Square
class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess game for trial')
        self.squares=[]
        self.show_background()

    def show_background(self):

        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BLACK # Black for even sum, space for odd
                square=Square(row,col,color)
                square.set_main_screen(self.screen)
                square.show_square()
                self.squares.append(square)

