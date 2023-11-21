#
# File: Game.py
# Description: Setup an odd or even boardgame class.
# Author: Arun Sharma
# Student ID: 110353025
# Email ID: shaay177
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

from Game import Game

class OddOrEven:

    def __init__(self, game):
        self._game = game

    def play_game(self):
        print("in Play_game")
        print(f"test {self._game.numPlayers}")
        self._game.select_num_player(1, 1)
        self._game.add_player()

        print(f"Hey {self._game.player[0]}")

