#
# File: Game.py
# Description: Setup the game class.
# Author: Arun Sharma
# Student ID: 110353025
# Email ID: shaay177
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

from Player import Player

class Game:

    GAMELIST = {"o": "Odd-or-Even", "m" : "Maxi", "b" : "Bunco"}

    def __init__(self, regPlayers):
        self._player = set()
        self._gameOver = False
        self._regPlayers = regPlayers
    
    @property
    def player(self):
        return self._player
    
    @property
    def gameOver(self):
        return self._gameOver
    
    def game_menu(self):
        print("\nWhich game would you like to play?")
        print(" (o) Odd-or-Even")
        print(" (m) Maxi")
        print(" (b) Bunc")

    def select_game(self, choose_game = "x"):
        while choose_game.lower() not in self.GAMELIST:
            self._game_menu()
            choose_game = input("> ")
        
