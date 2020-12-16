import pygame
from board import Board
import pygame.font


class Grid:
    """Class to draw the sudoku grid"""

    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.board = Board()

        # Dimensions of each square
        self.box_dim = self.settings.box_dim
        self.sq_colour = self.settings.bg_colour
        self.text_colour = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 40)

        # Dimensions of each line
        self.colour = self.settings.line_colour
        self.thick_line = self.settings.thick_line
        self.thin_line = self.settings.thin_line
        self.vertical = self.settings.vertical_length
        self.horizontal = self.settings.horizontal_length
        self.number = '0'
        self.font = pygame.font.SysFont(None, 38)

    def _draw_nsqs(self):
        """Function to draw the number square"""
        for i in range(0, 9):
            for j in range(0, 9):
                if i % 3 == 0:
                    if self.board.brd[i][j] != 0:
                        self.rect = pygame.Rect((i * self.box_dim)+3, (j * self.box_dim)+3, self.box_dim, self.box_dim)
                        self.msg_image = self.font.render(str(self.board.brd[i][j]), True, self.text_colour, self.sq_colour)
                        self.msg_image_rect = self.msg_image.get_rect()
                        self.msg_image_rect.center = self.rect.center
                    else:
                        self.rect = pygame.Rect((i * self.box_dim)+3, (j * self.box_dim)+3, self.box_dim, self.box_dim)
                        self.msg_image = self.font.render(' ', True, self.text_colour, self.sq_colour)
                        self.msg_image_rect = self.msg_image.get_rect()
                        self.msg_image_rect.center = self.rect.center
                    self.screen.fill(self.sq_colour, self.rect)
                    self.screen.blit(self.msg_image, self.msg_image_rect)
                else:
                    if self.board.brd[i][j] != 0:
                        self.rect = pygame.Rect((i * self.box_dim)+1, (j * self.box_dim)+3, self.box_dim, self.box_dim)
                        self.msg_image = self.font.render(str(self.board.brd[i][j]), True, self.text_colour, self.sq_colour)
                        self.msg_image_rect = self.msg_image.get_rect()
                        self.msg_image_rect.center = self.rect.center
                    else:
                        self.rect = pygame.Rect((i * self.box_dim)+1, (j * self.box_dim)+3, self.box_dim, self.box_dim)
                        self.msg_image = self.font.render(' ', True, self.text_colour, self.sq_colour)
                        self.msg_image_rect = self.msg_image.get_rect()
                        self.msg_image_rect.center = self.rect.center
                    self.screen.fill(self.sq_colour, self.rect)
                    self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw(self):
        # Draw the grid
        for i in range(0, self.settings.screen_width, int(self.box_dim * 3) + 2):
            pygame.draw.rect(self.screen, self.colour, pygame.Rect(i, 0, self.thick_line, self.vertical))
            pygame.draw.rect(self.screen, self.colour, pygame.Rect(0, i, self.horizontal, self.thick_line))
            c = int(0)
            for j in range(i + self.box_dim + 3, int(self.settings.screen_width), self.box_dim):
                pygame.draw.rect(self.screen, self.colour, pygame.Rect(j, 0, self.thin_line, self.vertical))
                pygame.draw.rect(self.screen, self.colour, pygame.Rect(0, j, self.horizontal, self.thin_line))
                c += 1
                if c == 3:
                    break
        # self._draw_nsqs()
