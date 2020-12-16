class Settings:
    """A class to store all the settings of the game"""

    def __init__(self):
        self.screen_width = 603
        self.screen_height = 800
        self.bg_colour = (244, 244, 223)

        # Gird Lines Characteristics
        self.thick_line = 3
        self.thin_line = 1
        self.horizontal_length = self.vertical_length = self.screen_width
        self.line_colour = (0, 0, 0)
        self.box_dim = int(round((self.screen_width - 18) / 9) + 1)

        # Text Characteristics
        self.text_colour = (0, 0, 0)
