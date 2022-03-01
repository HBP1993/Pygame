import pygame
#import pygame module for defining the class 

from pygame.sprite import Sprite

class Ship(Sprite):
    #A class to manage the ship 
    
    def __init__(self, ai_game):
        #Initialize the ship and set its starting position -
        #this is give access to  the game resources defined in AlienInvasion
        super().__init__()
        self.screen = ai_game.screen # Assigning the screen to the attribute of ship
        #to access all methods of this class
        
        self.settings = ai_game.settings
        #We create a settings attribute for Ship, so we can use it in update()
        
        
        
        self.screen_rect = ai_game.screen.get_rect()
        #we access the screen’s rect attribute using the get_rect() method
        #this will place ship in the correct location
        
        #load the ship image and get its rect. 
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect() 
        #call get_rect() to access the ship surface’s rectangle attribute so we can later use it 
        #to place the ship
        
        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        
        
        # Store a decimal value for the ship's horizontal position.
        #need to assign the position to a variable that can store a decimal value.
        #self.x attribute that can hold decimal values
        self.x = float(self.rect.x)
        
        
        #movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        #self.moving_right attribute in the __init__() method and set it  to False initially
        #adding update() move the ship right if the flag is true
        #update the ship's position based on the movement flag
         
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #. If the value of right side is less than the value returned by
            # self.screen _rect.right, the ship hasn’t reached the right edge of the screen
            
            
            self.x += self.settings.ship_speed 
            #from ship class: update the ship's x value, not the rect.
            
            
            
        if self.moving_left and self.rect.left > 0:
            #if the value of the left side of the rect is greater than zero,
            # the ship hasn’t reached the left edge of the screen
            self.x -= self.settings.ship_speed
            #from ship class: update the ship's x value, not the rect.
        
        # Update rect object from self.x.
        self.rect.x = self.x
        
    def blitme(self):
        #draw the ship image at its current location by self.rect
        self.screen.blit(self.image, self.rect)
        
        
    def center_ship(self):
        #Center the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)