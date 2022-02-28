import pygame
#import pygame module for defining the class 

class Ship:
    #A class to manage the ship 
    
    def __init__(self, ai_game):
        #Initialize the ship and set its starting position -
        #this is give access to  the game resources defined in AlienInvasion
        
        self.screen = ai_game.screen # Assigning the screen to the attribute of ship
        #to access all methods of this class
        
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
        
        #movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        #self.moving_right attribute in the __init__() method and set it  to False initially
        #adding update() move the ship right if the flag is true
        #update the ship's position based on the movement flag
        if self.moving_right:
            self.rect.x += 1
            
        if self.moving_left:
            self.rect.x -= 1
        
        
    def blitme(self):
        #draw the ship image at its current location by self.rect
        self.screen.blit(self.image, self.rect)
        