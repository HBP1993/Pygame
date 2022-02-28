import sys

import pygame


from settings import Settings   #to make instance of setting in the project and access setting
from ship import Ship    #to create a ship and call the ship's blitm() mathod 
from bullet import Bullet   #



class AlienInvasition:
    #creat a class alieninvasition to manage game assets and behavior
    
    
    def __init__(self):
        #Initialize the game, and create game resources.
        
        pygame.init() #initialize the background setting
        
        
        self.settings = Settings() #creating instance of Setting 
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        '''When creating the screen surface, passing a size of (0, 0) 
        and the parameter pygame.FULLSCREEN, this will figure out window size'''
        
        
        #self.screen = pygame.display.set_mode((1200, 800))
        
        
        # pygame.display.set_mode creates display window for the game
        # where games graphical element will be drawn
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        ## we create a screen and use width and height attributes of self.settings
        
        pygame.display.set_caption("Alien Invasion")
        
        
        self.ship = Ship(self)
        #self argument here is the instance of AlineInvasion and gives access to game's resources
        
        self.bullets = pygame.sprite.Group()
        
        
        
        
    def run_game(self):
        
        #start the main loop for the page
        while True:
            self._check_events()
            self.ship.update() #ships position will be updated after checked for keyword events before update the screen
            self._update_bullets()
            self._update_screen() #updating the screen
            
    def _check_events(self): #simplyfying the run_game method
        
        #responding to keypresses and mouse events or whether player make any movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            #SHIP MOVEMENT    
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        #respond to keypress
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True #set moving_right to true
            #If a KEYDOWN event occurs for the K_RIGHT key, we set moving_right to True.
            
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            #If a KEYDOWN event occurs for the K_LEFT key, we set moving_left to True.
          
        elif event.key == pygame.K_q: #press q to quit the game
            sys.exit()
            
        elif event.key == pygame.K_SPACE: #call bullet when spacebar is pressed
            self._fire_bullet()
            
            
    
    
    def _check_keyup_events(self, event):
        #respond to key releases    
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False #moving right to false
            #If a KEYUP event occurs for the K_RIGHT key, we set moving_right to false.       
                   
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            #If a KEYUP event occurs for the K_LEFT key, we set moving_left to False.
                    
        #if the right arrow key pressed, move the ship to the right
        #self.ship.rect.x += 1
    
    def _fire_bullet(self):
        #Create a new bullet and add it to the bullets group.
        
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    
    
    def _update_bullets(self):
        #Update position of bullets and get rid of old bullets.
        # Update bullet positions.
        self.bullets.update() #it will automatically calls update() for each sprite in the group.
            
        #get rid of bullets that have disappeared
        for bullet in self.bullets.copy(): # it enables to modify bullets inside the loop.
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        
        
        #print(len(self.bullets))
        
    
         
    def _update_screen(self):
        #update image on the screen, and flip to the new screen 
              
        self.screen.fill(self.settings.bg_color) 
        #self.settings to access background color when filling the screen 
        
        self.ship.blitme()
        #calling ship.blitme() to appear the ship on top of the background
        
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        #make the most recently drawn screen visible    
        pygame.display.flip()
                
if __name__ == '__main__':
    ai = AlienInvasition()
    ai.run_game()
    