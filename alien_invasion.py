#First, we’ll create an empty Pygame window.


import sys
import pygame
#Adding settings
from settings import Settings

#Drawing ship
from ship import Ship

#refactoring the functions from main file
import game_functions as gf

def run_game():
    pygame.init() #initializing the game
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) 
    #Create a screen object
    #pygame.display.set_mode(1200,700)
    pygame.display.set_caption("Alien Invasion")
    
    #make ship
    ship = Ship(screen)
    #initializing color
    #start main loop
    while True:
        #watch for the keyboard and mouse events
        gf.check_events(ship)
        
        ship.update() #for every event detection
        
        #updating screen
        gf.update_screen(ai_settings,screen,ship)
        

run_game()



