from coordinates import make_step_back_for_x_or_y, make_step_forwafd_for_x_or_y
import constants
import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resourses/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (constants.WIDTH / 2, constants.HEIGHT / 2)       
        self.width: int = 40
        self.height: int = 40
    
    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = make_step_back_for_x_or_y(self.rect.x, constants.WALL_SIZE)
        if keys[pygame.K_RIGHT]:
            self.rect.x = make_step_forwafd_for_x_or_y(self.rect.x, constants.WIDTH-constants.WALL_SIZE)
        if keys[pygame.K_UP]:
            self.rect.y = make_step_back_for_x_or_y(self.rect.y, constants.WALL_SIZE)
        if keys[pygame.K_DOWN]:
            self.rect.y = make_step_forwafd_for_x_or_y(self.rect.y, constants.HEIGHT-constants.WALL_SIZE )

    def has_met_the_chest():
        pass


class Wall(pygame.sprite.Sprite):
    def __init__(self, x = 0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resourses/wall.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width: int = constants.WALL_SIZE
        self.height: int = constants.WALL_SIZE
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, (self.rect.x, self.rect.y))


class Chest(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resourses/chest.png")
        self.rect = self.image.get_rect()
        self.rect.center = (constants.WIDTH / 2, constants.HEIGHT / 2)       
        self.width: int = 40
        self.height: int = 40
    
    def update(self) -> None:
            step = 15
            self.rect.x += random.choice([-1, 1])*step
            self.rect.y += random.choice([-1, 1])*step

            if self.rect.x > constants.WIDTH-2*constants.WALL_SIZE:
                self.rect.x -= 2*step
            if self.rect.x  < 2*constants.WALL_SIZE:
                self.rect.x += 2*step
         
            if self.rect.y > constants.HEIGHT-2*constants.WALL_SIZE:
                self.rect.y -= 2*step
            if self.rect.y  < 2*constants.WALL_SIZE:
                self.rect.y += 2*step
         