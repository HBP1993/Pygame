import sys

from time import sleep
#this helps to  pause the game for a moment when the ship is hit

import pygame


from settings import Settings   #to make instance of setting in the project and access setting
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship    #to create a ship and call the ship's blitm() mathod 
from bullet import Bullet   #
from alien import Alien #




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
        
        # Create an instance to store game statistics
        self.stats = GameStats(self)
        
        #Create an instance to store game statistics,
        #and create a scoreboard.
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self)
        #self argument here is the instance of AlineInvasion and gives access to game's resources
        
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group() #creating instance for Alian
        
        self._create_fleet()
        
        ## Make the Play button
        self.play_button = Button(self, "Play")
        
        
        
        
        
    def run_game(self):
        
        #start the main loop for the page
        while True:
            self._check_events()
            
            if self.stats.game_active: #parts that should run only when the game is active
                self.ship.update() #ships position will be updated after checked for keyword events before update the screen
                self._update_bullets()
                self._update_aliens()
                
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
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    
    
    def _check_play_button(self, mouse_pos):
        #Start a new game when the player clicks Play.
        
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
        ###if self.play_button.rect.collidepoint(mouse_pos):
            
            
            self.settings.initialize_dynamic_settings()
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()  # after resetting the game stats when starting a new game and start from 0
            self.sb.prep_level()
            self.sb.prep_ships()

            
            
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            
            ## Hide the mouse cursor.
            pygame.mouse.set_visible(False)
    
    
              
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
        
        self._check_bullet_alien_collisions()
    
    
    
        
    def _check_bullet_alien_collisions(self):
        #"Respond to bullet-alien collisions.
        # Remove any bullets and aliens that have collided.

        
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens) #making sure to score all hits
            #self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:   #check whether the aliens group is empty
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            
            #increase the game’s tempo by calling increase_speed() 
            self.settings.increase_speed()
            
            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()
            
    
    
    
    
    
        
    
    def _update_aliens(self):
        
        #Check if the fleet is at an edge, then update the positions of all aliens in the fleet.
        self._check_fleet_edges()
        #Update the positions of all aliens in the fleet and it calls ecah aline's update method
        self.aliens.update()
        
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            #If no collisions occur, spritecollideany() returns None and the if block 
            #will not execute
            self._ship_hit() #print function replaced
            #print("Ship hit!!!")
            #if collided with the ship, it will execute ship    
            
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()    
    
    
    
    
    
    
    def _create_fleet(self):
        #Create the fleet of aliens. or 
        
        #make an alien
        alien = Alien(self) #creat an alien
        #self.aliens.add(alien)
        
        
        # create an alien and find the number of aliens in a row.
        # spacing between each alien is equal to one alien weidth
        alien_width, alien_height = alien.rect.size
        # get the alien’s width & height from its rect attribute 
        
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # calculate the horizontal space available for aliens 
        
        number_aliens_x = available_space_x // (2 * alien_width)
        #calculate the number of aliens that can fit into that space.
        
        
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        
        
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            #To create multiple rows, we use two nested loops
            #inner loop creates the alian in one row and outer loop count from zero
        
            # Create the first row of aliens.
            # set up a loop that counts from 0 to the number of aliens we need to make
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            
    
    
    
    
    #this defines the alien number that’s currently being created.      
    def _create_alien(self, alien_number, row_number):
        #Create an alien and place it in the row.
            
        # Create an alien and place it in the row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size   
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
            

    
    
    
    
    def _check_fleet_edges(self):
        #Respond appropriately if any aliens have reached an edge.
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
     
     
     
            
    def _change_fleet_direction(self):
        #Drop the entire fleet and change the fleet's direction.
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 
    
    
    
    
    
    
    def _ship_hit(self):
        # _ship_hit() coordinates the response when an alien hits a ship
        #Respond to the ship being hit by an alien
        
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard. 
            self.stats.ships_left -= 1
            #the number of ships left is reduced by 1
            self.sb.prep_ships()
            
            # Get rid of any remaining aliens and bullets after hit or reduced by 1
            self.aliens.empty()
            self.bullets.empty()
        
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
        
            # Pause
            sleep(0.5)
            
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    
    
    
    
    def _check_aliens_bottom(self):
        #Check if any aliens have reached the bottom of the screen
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                ## Treat this the same as if the ship got hit.
                self._ship_hit()
                break

       
    def _update_screen(self):
        #update image on the screen, and flip to the new screen 
              
        self.screen.fill(self.settings.bg_color) 
        #self.settings to access background color when filling the screen 
        
        self.ship.blitme()
        #calling ship.blitme() to appear the ship on top of the background
        
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen) 
        #To make the alien appear, we need to call the group’s draw() method   
        
        # Draw the score information.
        self.sb.show_score()
        
        
        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        #make the most recently drawn screen visible    
        pygame.display.flip()
                
if __name__ == '__main__':
    ai = AlienInvasition()
    ai.run_game()
    