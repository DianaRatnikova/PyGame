import constants
import models
import pygame


def make_wall_coordinates_list() -> list[list[int]]:
    x = 0
    y = 0
    wall_coordinates_list = []

    number_of_horisontal_blocks = constants.WIDTH // constants.WALL_SIZE
    number_of_vertical_blocks = constants.HEIGHT // constants.WALL_SIZE

    for _ in range(number_of_horisontal_blocks):
        wall_coordinates_list.append([x, 0])
        wall_coordinates_list.append([x, constants.HEIGHT - constants.WALL_SIZE])
        x+=constants.WALL_SIZE
       
    for _ in range(number_of_vertical_blocks - 2):
        y += 20
        wall_coordinates_list.append([0, y])
        wall_coordinates_list.append([constants.WIDTH - constants.WALL_SIZE, y])
                  
    return wall_coordinates_list


def move_player(player: models.player.Player, walls: models.wall.Wall) -> None:
    previous_player_topleft = player.rect.topleft
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect = player.rect.move(-constants.STEP, 0)
    if keys[pygame.K_RIGHT]:
        player.rect = player.rect.move(constants.STEP, 0)
    if keys[pygame.K_UP]:
        player.rect = player.rect.move(0, -constants.STEP)
    if keys[pygame.K_DOWN]:
        player.rect = player.rect.move(0, constants.STEP)
    
    if pygame.sprite.spritecollide(player, walls, dokill=False):
        player.rect.topleft = previous_player_topleft