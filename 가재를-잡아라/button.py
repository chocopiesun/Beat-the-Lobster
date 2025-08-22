import pygame

pygame.init()

class Button:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)   
    
    def is_clicked(self, mouse_pos, event):
        return self.rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP