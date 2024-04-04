import pygame
from constant import *
class Square:
    def __init__(self,row,col,color):
        self.row=row
        self.col=col
        self.color=color
        self.square_size=SQUARE_SIZE
        self.value=0
        self.position=(self.row*self.square_size,self.col*self.square_size)
        self.surface=pygame.Surface((self.square_size,self.square_size))
        self.surface.fill(self.color)
        self.screen=None
        self.piece=None

    def show_square(self):
        if self.screen:
            self.screen.blit(self.surface,self.position)
        

    def set_main_screen(self,screen):
        self.screen=screen

    def is_empty(self):
        return self.value==0

    def add_piece(self,piece):
        self.piece=piece
        if self.piece:
            image=self.piece.image
            self.value=self.piece.value
            self.image_rect =image.get_rect()
            self.image_rect.center=(SQUARE_SIZE//2,SQUARE_SIZE//2)
            self.surface.blit(image,self.image_rect)
            self.show_square()
