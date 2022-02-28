from re import S
import pygame

from pygame.sprite import Sprite #The Bullet class inherits from Sprite
#related elements can be grouped together by using sprite

class Bullet(Sprite):
    #A class to manage bullets fired from the ship
    
    def __init__(self, ai_game):
        #Create a bullet object at the ship's current position.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0, 0) and then set correct position.
        # build a rect from scratch using the pygame.Rect() class.
        
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        
        self.rect.midtop = ai_game.ship.rect.midtop
        #set the bullet’s midtop attribute to match the ship’s midtop attribute
        #and make it look like bullet fired from the ship
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        
        
    def update(self): #The update() method manages the bullet’s position.
        #move the bullet up the screen
        
        #update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        
        # Update the rect position. and use the value of self.y to set the value of self.rect.y
        self.rect.y = self.y
        
    def draw_bullet(self):
        #Draw the bullet to the screen. draw.rect() function fills the part of the screen
        # defined by the bullet’s rect with the color stored in self.color
        pygame.draw.rect(self.screen, self.color, self.rect)