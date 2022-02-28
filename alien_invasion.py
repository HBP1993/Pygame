import sys

import pygame


from settings import Settings   #to make instance of setting in the project and access setting
from ship import Ship    #to create a ship and call the ship's blitm() mathod 



class AlienInvasition:
    #creat a class alieninvasition to manage game assets and behavior
    
    
    def __init__(self):
        #Initialize the game, and create game resources.
        
        pygame.init() #initialize the background setting
        
        
        self.settings = Settings() #creating instance of Setting 
        self.screen = pygame.display.set_mode((1200, 800))
        
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) # we create a screen and use width and height attributes of self.settings
        
        pygame.display.set_caption("Alien Invasion")
        
        
        self.ship = Ship(self)
        #self argument here is the instance of AlineInvasion and gives access to game's resources
        
    def run_game(self):
        
        #start the main loop for the page
        while True:
            self._check_events()
            self.ship.update() #ships position will be updated after checked for keyword events before update the screen
            self._update_screen() #updating the screen
            
    def _check_events(self): #simplyfying the run_game method
        
        #responding to keypresses and mouse events or whether player make any movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            #SHIP MOVEMENT    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True #set moving_right to true
                    #If a KEYDOWN event occurs for the K_RIGHT key, we set moving_right to True.
                    
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                    #If a KEYDOWN event occurs for the K_LEFT key, we set moving_left to True.
            
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False #moving right to false
                    #If a KEYUP event occurs for the K_RIGHT key, we set moving_right to false.
                
                   
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                    #If a KEYUP event occurs for the K_LEFT key, we set moving_left to False.
                    
                    #if the right arrow key pressed, move the ship to the right
                    self.ship.rect.x += 1
            
    def _update_screen(self):
        #update image on the screen, and flip to the new screen 
               
        self.screen.fill(self.settings.bg_color) 
        #self.settings to access background color when filling the screen 
        
        self.ship.blitme()
        #calling ship.blitme() to appear the ship on top of the background
        
        
        
            
        #make the most recently drawn screen visible    
        pygame.display.flip()
                
if __name__ == '__main__':
    ai = AlienInvasition()
    ai.run_game()
    