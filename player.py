import pygame
import sys
import os
import random



if __name__ == "__main__":

    size = 640, 320
    width, height = size
    GREEN = (150, 255, 150)
    RED = (255, 0, 0)
    clock = pygame.time.Clock()


    pygame.init()
    screen = pygame.display.set_mode(size)
    running = True

    chest = pygame.image.load("resourses/chest.png")
    chest_x = 100
    chest_y = 100

    player = pygame.image.load("resourses/player.png")
    player_x = 60
    player_y = 90

    
    direction = {pygame.K_LEFT: (-20, 0), 
           pygame.K_RIGHT: (20, 0), 
           pygame.K_UP: (0, -20), 
           pygame.K_DOWN: (0, 20) }
    
    chest_step = 20
    sign = [-1, 1]
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in direction:
                    step_direction = direction[event.key]
                    player_x += step_direction[0]
                    player_y +=step_direction[1]


        chest_x += random.choice([-1, 1])*chest_step
        if chest_x<0:
            chest_x += 2*chest_step
        if chest_x > width:
            chest_x -= 2*chest_step

        chest_y += random.choice([-1, 1])*chest_step
        if chest_y<0:
            chest_y += 2*chest_step
        if chest_y > height:
            chest_y -= 2*chest_step

        rect_chest = chest.get_rect()
        screen.fill(GREEN)
        pygame.draw.rect(screen, RED, rect_chest, 1)
        screen.blit(chest, (chest_x, chest_y))
        screen.blit(player, (player_x, player_y))
        pygame.display.update()
        
        clock.tick(60)

    pygame.quit()