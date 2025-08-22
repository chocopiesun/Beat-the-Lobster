import pygame

pygame.init()

class Base:
    def __init__(self, x, y, health, sprites, type):
        self.type = type + "_base"
        self.name = 'enemy_base'

        self.x = x
        self.y = y

        self.state = 'peace'

        self.health = health
    
        self.sprites = sprites
        self.current_sprite = self.sprites[0][0]
        self.rect = self.current_sprite.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        if self.state == 'peace':
            self.current_sprite = self.sprites[0][0]

        screen.blit(self.current_sprite, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)

        if self.health <= 0:
            self.state = 'death'
            self.current_sprite = self.sprites[1][0]

