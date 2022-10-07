import imghdr
import pygame
import pygame.freetype

from letter import Letter

class Word:
    ''' creating/generating word '''
    # remove later ... after we input files
    words = ['egg','ham','monster','fruit','keyboard','valuable']
    
    # TODO wpm_game is unknown ... idk why
    def __init__(self, wpm_game):
        ''' initialize the word and set its starting position'''
        # super().__init__() # might need this? not sure.
        self.screen = wpm_game.screen
        self.screen_rect = wpm_game.screen.get_rect()

        # generate word (using built-in default font)
        default_font = pygame.freetype.get_default_font()
        self.word = pygame.font.Font(default_font, 10)
        # self.img = self.word.render('hello',True, (255,255,255))
        self.imgs = []
        
        
        # place word in center of screen
        self.rect = self.screen_rect.center
    
    def generate_words(self):
        ''' generate words for user to input (to measure wpm)'''
        # TODO, read from file input from free books and insert words
        # for now, we use a given list of words
        imgs = []
        for word in self.words:
            imgs.append(self.word.render(word,True, (255,255,255)))   
        self.imgs = imgs
        return self.imgs

        
    def blitme(self):
        ''' Draw words ... '''    
        self.screen.blit(self.imgs, self.rect)
    
    
    
    
    # def has_next(self):
    #     if next(self):
    #         return True
    #     else:
    #         return False
        
    # def next(self):
    #     if has_next:
    #         ''' return next word '''
    #     else:
    #         return None
        
    
    
    
    
        
        