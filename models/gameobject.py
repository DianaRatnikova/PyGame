import pygame
import constants

class GameObject(pygame.sprite.Sprite):
    filepath : str
    width: int
    height: int

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(self.filepath)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




