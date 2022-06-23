import pygame.font
class Text:
    dark_color = (5, 5, 5)
    light_color = (20, 20, 20)
    text_color = (255, 255, 255)
    font = pygame.font.SysFont('TTF', 20)
    text = 0
    def __init__(self, string1):
        self.text = self.font.render(string1, True, self.text_color)

class Button:
    width=60
    hight=30




