class Settings:
    """A class to store all setting for Alien Invasion"""
    
    def __init__(self):
        '''Instializaing game settings'''
        
        #screen setting
        #self.screen_width = 1000 #no need to keep this after making it full screen
        #self.screen_height = 600
        self.bg_color = (230, 230, 230) #tuple 
        
        #ship setting
        self.ship_speed = 1.5
        self.ship_limit = 3
        
         
        #bullet Setting
        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3 #This limits the player to three bullets at a time.
        
        #aline settings
        self.alien_speed = 1.0 #control the speed of each alien
        self.fleet_drop_speed = 10 #The setting fleet_drop_speed controls how quickly the fleet drops down 
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        #control how quickly the game speeds up
        
        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        
        #the values for attributes that need to change throughout the game
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        #Initialize settings that change throughout the game.
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Scoring
        self.alien_points = 50
        
    #To increase the speeds of the ship, bullets, and aliens each time the player reaches a new level
    def increase_speed(self):
        #increase speed setting
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale) #increase the point value of each hit
        print(self.alien_points)
        
        
        
    
   