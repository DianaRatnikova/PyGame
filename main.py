from classes import Player, Chest
import constants
import pygame
from sprites import add_walls_to_all_sprites


if __name__ == "__main__":

    pygame.init() 
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT)) 
    pygame.display.set_caption("GAME")
    clock = pygame.time.Clock() 
    all_sprites = pygame.sprite.Group()

    player = Player()
    chest = Chest()
    add_walls_to_all_sprites(all_sprites)
    
    all_sprites.add(player)
    all_sprites.add(chest)

    print(f"{type(all_sprites) = }")

    running = True 

    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
 
        all_sprites.update() 
        screen.fill("purple")
        all_sprites.draw(screen)
        pygame.display.flip() 

        clock.tick(60)

    pygame.quit()