import pygame
from game_parametres import coin_info, object_colors

class Colored_coin(pygame.sprite.Sprite):
    def __init__(self, color, position, column):
        super(Colored_coin, self).__init__()
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], coin_info.COIN_DIMENSION, coin_info.COIN_DIMENSION)
        self.position = position
        self.column = column
    
    
    def s(self):
        self.surf = pygame.Surface((coin_info.COIN_DIMENSION, coin_info.COIN_DIMENSION))
        self.surf.fill(self.color)
        return self.surf

class Blocked_space(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Blocked_space, self).__init__()
        self.rect = pygame.Rect(position[0], position[1], coin_info.COIN_DIMENSION, coin_info.COIN_DIMENSION)
        self.position = position
 
    def s(self):
        self.surf = pygame.Surface((coin_info.COIN_DIMENSION, coin_info.COIN_DIMENSION))
        self.surf.fill(object_colors.BLACK)
        return self.surf

class Empty_space(pygame.sprite.Sprite):
    def __init__(self, position, column):
        super(Empty_space, self).__init__()
        self.rect = pygame.Rect(position[0], position[1], coin_info.COIN_DIMENSION, coin_info.COIN_DIMENSION)
        self.position = position
        self.column = column
    
    def s(self):
        self.surf = pygame.Surface((coin_info.COIN_DIMENSION, coin_info.COIN_DIMENSION))
        self.surf.fill(object_colors.GREY)
        return self.surf

class Column_color(pygame.sprite.Sprite):
    def __init__(self, color, position, column):
        super(Column_color, self).__init__()
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], coin_info.COIN_DIMENSION, coin_info.COIN_DIMENSION)
        self.position = position
        self.column = column
    
    
    def s(self):
        self.surf = pygame.Surface((coin_info.COIN_DIMENSION, coin_info.COIN_DIMENSION))
        self.surf.fill(self.color)
        return self.surf