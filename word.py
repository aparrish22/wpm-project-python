
class Word:
    
    def __init__(self, wpm_game):
        ''' initialize the word and set its starting position'''
        self.screen = wpm_game.screen
        self.screen_rect = wpm_game.screen.get_rect()
        
    def blit_me(self):
        ''' Draw words ... '''    
        self.screen.blit(...)
        pass
    
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
        
    
    
    
    
        
        