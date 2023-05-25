import pygame
import sys
import os

STEP = 5
dt = 1
RED = (255, 0, 0)

def make_step_back_for_x_or_y(coord: float, dimention: int) -> float:
    result = coord - STEP*dt
    return result if result > dimention else coord


def make_step_forwafd_for_x_or_y(coord: float, dimention: int) -> float:
    result = coord + STEP*dt
    return result if result < dimention - STEP*dt else coord


def change_coord_of_player(player_position: pygame.math.Vector2, keys: pygame.key.ScancodeWrapper) -> pygame.math.Vector2:
    if keys[pygame.K_LEFT]:
        player_position.x = make_step_back_for_x_or_y(player_position.x, 0)
    if keys[pygame.K_RIGHT]:
        player_position.x = make_step_forwafd_for_x_or_y(player_position.x, screen.get_width())
    if keys[pygame.K_UP]:
        player_position.y = make_step_back_for_x_or_y(player_position.y, 0)
    if keys[pygame.K_DOWN]:
        player_position.y = make_step_forwafd_for_x_or_y(player_position.y, screen.get_height())
    return player_position



if __name__ == "__main__":
# pygame setup 
    pygame.init() 
    screen = pygame.display.set_mode((500, 500)) 
    clock = pygame.time.Clock() 
    running = True 

    player = pygame.image.load("resourses/player.png")
    walls = pygame.image.load("resourses/wall.png")
    player_position = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
    wall_position = pygame.Vector2(0, 0)
    player_rect = player.get_rect() 

    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
    
 
        keys = pygame.key.get_pressed()
        
        player_position = change_coord_of_player(player_position, keys)
        screen.fill("purple")
        
        pygame.draw.rect(screen, RED, player_rect, 1)
        screen.blit(player, (player_position.x, player_position.y))
        pygame.display.update()
        #pygame.display.flip() 
        clock.tick(60) 
    pygame.quit()