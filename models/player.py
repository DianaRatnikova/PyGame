import pygame
import constants
from models.gameobject import GameObject


class Player(GameObject):

    filepath = "resourses/player.png"
    width =  40
    height =  40

    def has_met_the_chest(self, another_object: "GameObject") -> bool:
        return self.rect.colliderect(another_object.rect)

