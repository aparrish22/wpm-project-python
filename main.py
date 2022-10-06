# TODO finish project(s) in kindle book
#from turtle import Screen
import pygame
import pygame.freetype
from pygame.locals import * # todo, delete?
import sys
import time
import random

# my modules & classes
from player import Player
from word_character import Word
from settings import Settings

class Game:
    ''' wpm main screen game/app '''
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        # The object we assigned to self.screen is called a surface
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Words per Minute")
        self.bg_color = (20, 95, 45)
        
    def run_game(self):
        ''' Start the main loop for the game. '''
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self._update_screen()
    
    def _update_screen(self):
        ''' Update images on the screen, and flip to the new screen. '''
        
        # redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        
        # make the moost recently drawn screen visible
        pygame.display.flip()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
    
    def read_input(self):
        ''' Read input and measure WPM'''
        ''' may need this elsewhere???'''
        pass
    
    def choose_game_mode(self):
        ''' ask for user input via button to choose a game mode'''
        pass
    
    def generate_words(self):
        ''' generate words for user to input (to measure wpm)'''
        pass
    
    def generate_characters(self):
        ''' generate character for user to input (to measure wpm)'''
        pass
    
    def generate_page(self):
        ''' Generate page(s) as user completes every word/char on current page.'''
        pass
           

game = Game()
game.run_game()
        
        
                    
           

 


        # pygame.display.init()
        # pygame.init()
        
        # # variables for screen
        # w = 800
        # h = 600
        # dimensions = [w,h]
        # background_color = (27, 99, 31)
        # flags = pygame.SHOWN | pygame.RESIZABLE
        # running = True
        
        # pygame.display.set_mode(dimensions, flags)
        # pygame.display.set_caption('Words Per Minute App')
        # pygame.Surface(dimensions, flags)
        
        # # self.screen = pygame.fill(background_color)
        # pygame.Surface.fill(background_color)
        
        # # update
        # pygame.display.flip()
        
        # while running:
        #     # event queue
        #     for event in pygame.event.get():
        #         # check for QUIT event
        #         if event.type == pygame.QUIT:
        #             running = False
        #             pygame.QUIT
