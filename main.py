
from models.chest import Chest
from models.player import Player
from models.wall import Wall

from coordinates import move_player, make_wall_coordinates_list
import constants
import pygame



if __name__ == "__main__":

    pygame.init() 
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT)) 
    pygame.display.set_caption("GAME")
    clock = pygame.time.Clock() 
    all_sprites = pygame.sprite.Group()

    player = Player(int(constants.WIDTH / 2), int(constants.HEIGHT / 2))
    chest = Chest(100, 100)
    walls = pygame.sprite.Group([Wall(x, y) for (x, y) in make_wall_coordinates_list()])

    all_sprites.add(player)
    all_sprites.add(chest)
    all_sprites.add(walls)

    running = True 

    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
        
        all_sprites.update()    
        screen.fill("purple")
        all_sprites.draw(screen)

        if not player.rect.colliderect(chest.rect):
            move_player(player, walls)
        pygame.display.flip() 

        clock.tick(60)

    pygame.quit()