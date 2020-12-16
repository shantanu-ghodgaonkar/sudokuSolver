import sys
import pygame
from settings import Settings
from grid import Grid
from board import Board


# GitHub comment test 1

class Game:
    """Class to monitor and manage all assets of the game"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.grid = Grid(self)
        self.board = Board()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self.screen.fill(self.settings.bg_colour)
            self.grid.draw()
            pygame.display.flip()


if __name__ == '__main__':
    g = Game()
    g.run_game()
