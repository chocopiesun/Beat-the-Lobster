import pygame
from constants import *
import time
from health_bar import HealthBar

pygame.init()

class Player:
    def __init__(self,name, width, height, speed, damage, attack_range, health, attack_cooltime, sprites):
        self.type = 'player'
        self.name = name
        self.state = 'moving'

        if self.name == 'lobster':
            self.x = 1350
            self.y = 380
        else:
            self.x = 1350
            self.y = 350
        self.width = width
        self.height = height
        self.sprites = sprites
        self.rect = self.sprites[0][0].get_rect()
        self.rect.topleft = (self.x, self.y)

        self.health = health
        self.speed = speed
        self.damage = damage
        self.attack_range = attack_range
        self.attack_cooltime = attack_cooltime
        self.recent_attack_time = 0
        self.target = None
        self.target_detection_box = pygame.Rect(self.x - self.attack_range, self.y, self.attack_range + self.width, self.height)

        self.image_index = 0

        self.health_bar = HealthBar(self.x + 10, self.y - 30, 100, 15, self.health)

    def draw(self, screen):
        if self.state == 'moving':
            if self.image_index >= 2 and self.name != "swallow":
                self.image_index = 0
            elif self.image_index >= 1 and self.name == "swallow":
                self.image_index = 0
            self.current_sprite = self.sprites[0][int(self.image_index)]
            self.image_index += 5 / FPS
        
        elif self.state == 'attacking':
            if self.image_index >= 2 and self.name != "swallow":
                self.image_index = 0
            elif self.image_index >= 6 and self.name == "swallow":
                self.image_index = 0
            self.current_sprite = self.sprites[1][int(self.image_index)]
            self.image_index += 5 / FPS
        
        screen.blit(self.current_sprite, (self.x, self.y))

        self.health_bar.update_health(self.health)
        self.health_bar.draw(screen)
    
    def move(self):
        if self.state == 'moving':
            self.x -= self.speed / FPS
            self.health_bar.x -= self.speed / FPS 
            if self.x <= 140:
                self.x = 140
                self.health_bar.x = 140
        
        self.rect.topleft = (self.x, self.y)
        self.target_detection_box.topleft = (self.x - self.attack_range, self.y)
    
    def attack(self, enemies):
        if self.target == None:
            for i in enemies:
                if self.target_detection_box.colliderect(i.rect):
                    self.target = i
                    self.state = 'attacking'
                    break
        
        if self.state == 'attacking':
            
            if time.time() - self.recent_attack_time >= self.attack_cooltime:
                self.recent_attack_time = time.time()
                self.target.health -= self.damage
                
                if self.target.health <= 0:
                    self.target = None
                    self.state = 'moving'
                    