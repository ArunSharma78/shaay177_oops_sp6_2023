#
# File: GameMaxi.py
# Description: Game Maxi code as per the rules set.
# Author: Arun Sharma
# Student ID: 110353025
# Email ID: shaay177
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

from Game import Game

class Maxi:

    def __init__(self, game, dice1, dice2):
        self._game = game
        self._dice1 = dice1
        self._dice2 = dice2
        self._pscore = dict()

    def play_game(self):
        self._game.select_num_player(3, 5)
        self._game.add_player()
        for p in self._game.player:
            self._dice1.throw_dice()
            self._dice1.generate_throw_strength()
            self._dice2.throw_dice()
            s1 = self._dice1.get_diceValue
            t1 = self._dice1.throwStrength
            self._dice2.set_throwStrength(t1)
            print(f"{self._dice1.get_dice_face()} {self._dice2.get_dice_face()}")