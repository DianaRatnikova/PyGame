import pygame
import constants
from models.gameobject import GameObject



class Wall(GameObject):
    filepath = "resourses/wall.png"
    width = constants.WALL_SIZE
    height = constants.WALL_SIZE
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, (self.rect.x, self.rect.y))
