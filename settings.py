class Settings:
    """A class to store all setting for Alien Invasion"""
    
    def __init__(self):
        '''Instializaing game settings'''
        
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230) #tuple 
        self.ship_speed = 1.5
        
        #bullet Setting 
        
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3 #This limits the player to three bullets at a time.