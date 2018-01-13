#part of refactoring alien_invasion.py preventing it to become lengthy and hard to follow

import sys

import pygame

#refactoring event checks from main file
def check_events(ship):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get(): #gets event from the queue
            if event.type == pygame.QUIT:
                sys.exit()
            
            #responding to keypresses
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move the ship to the right.
                    #ship.rect.centerx += 1
                    #adding the continuous moving functionality
                    ship.moving_right=True #we set moving right attribute to True till keydown(pressed)
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
            
            #as soon as the keyup(release) is detected, set moving_right attribute to false
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False
            
                    
                    
                    
#refactoring update_screen functionality
def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    #screen.fill(bg_color) #filling the background color
    ship.blitme() # blit the ship
    pygame.display.flip()

