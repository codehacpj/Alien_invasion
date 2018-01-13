#Ship module


import pygame

class Ship():
    def __init__(self,screen):
        """Initialize ship and set its starting position."""
        self.screen = screen
        
        
        #load ship image and get its rect
        
        self.image = pygame.image.load('ship.bmp') #returns a surface representing the ship
        self.rect = self.image.get_rect() #image as rectangle
        self.screen_rect = screen.get_rect() #screen as rectangle
        
        #start new ship at the bottom center of the screen
        
        self.rect.centerx = self.screen_rect.centerx #place image at center
        self.rect.bottom = self.screen_rect.bottom #place at the bottom of the screen
        
        
        #store a decimal value for the ship's center
        
        
        
        #To check the movement of the ship
        #Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement of flag."""
        #Update the ship's center value,not the rect.
        if self.moving_right:
            self.rect.centerx += 1#self.ai_settings.ship_speed_factor 
        if self.moving_left:
            self.rect.centerx -= 1#self.ai_settings.ship_speed_factor #-=1
        
        #update rect object from self.center
        
        
        
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect) #draw the self.image at self.rect
