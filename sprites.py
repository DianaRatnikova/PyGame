from coordinates import make_wall_coordinates_list
from classes import Wall
import pygame


def add_walls_to_all_sprites(all_sprites: pygame.sprite.Group) -> None:
    wall_coordinates_list = make_wall_coordinates_list()
    for coordinates in wall_coordinates_list:
        wall = Wall(coordinates[0], coordinates[1])
        all_sprites.add(wall)
