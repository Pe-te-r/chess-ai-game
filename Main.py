import pygame
from Game import Game


class Main:
    def __init__(self):
        self.game_running=True
        self.game=Game()
        self.screen=self.game.screen

    def main_loop(self):
        game=self.game
        game.show_background()
        
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running=False

            

            pygame.display.flip()



main=Main()
main.main_loop()
