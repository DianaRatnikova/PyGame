import pygame
import random
import constants
from models.gameobject import GameObject


class Chest(GameObject):
    filepath = "resourses/chest.png"
    x = int(constants.WIDTH / 2)
    y = int(constants.HEIGHT / 2)

    def update(self) -> None:
        step = 20
        self.rect.x += random.choice([-1, 1, 0])*step
        self.rect.y += 0#random.choice([-1, 1, 0])*step
        if self.rect.x > constants.WIDTH-2*constants.WALL_SIZE:
            self.rect.x -= 2*step
        if self.rect.x  < 2*constants.WALL_SIZE:
            self.rect.x += 2*step
     
        if self.rect.y > constants.HEIGHT-2*constants.WALL_SIZE:
            self.rect.y -= 2*step
        if self.rect.y  < 2*constants.WALL_SIZE:
            self.rect.y += 2*step

    