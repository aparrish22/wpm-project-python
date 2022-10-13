import time
from word import Word

class Player:
    ''' A user who wants to measure their WPM. '''
    player_name = ""
    accuracy = 0.0
    speed = 0.0
    wpm = 0
    
    def __init__(self, player_name, accuracy, speed, wpm, wpm_high_score=0.0):
        ''' initialize class variables '''
        ''' be able to restore player's saved scores for every init via json '''
        self.player_name = player_name
        self.wpm_high_score = wpm_high_score
        self.accuracy = accuracy
        self.speed = speed
        self.WPM = wpm
        
    def keyboard_input(self, character):
        ''' take input and check for successes and failures. '''
        # if (success input)
            # increment accuracy
            # add speed to WPM
            # move to next character
        # elif (failure input)
            # decrement acc
            # subtract speed to WPM
            # move to next character
            # Bonus: allow backtracking via BACKSPACE
        # else: 
            # if input non-character (example: ESC, F1, etc.): do nothing '''
            # pass(?) do nothing

    def measure_wpm(self, speed):
        ''' calculate wpm for the player based on speed '''
        
    def high_score_wpm(self, wpm):
        ''' save high_score (to json file) '''
        
    def set_player_name(self, player_name):
        self.player_name = player_name