#
# File: CommandLineInterface.py
# Description: This is the interface to connect various classes.
# Author: Arun Sharma
# Student ID: 110353025
# Email ID: shaay177
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

from Player import Player
from GameOddOrEven import OddOrEven
from GameMaxi import Maxi
from GameBunco import Bunco
from Game import Game
from Dice import Dice

class CommandLineInterface:
    GAMELIST = {"o": "Odd-or-Even", "m" : "Maxi", "b" : "Bunco"}

    def __init__(self):
        pass

    def display_greeting(self):
        print(f"Welcome to All-That-Dice!")
        print(f"Developed by Arun Sharma")
        print(f"COMP 1048 Object-Oriented Programming")

    def display_main_menu(self):
        print(f"\nWhat would you like to do?")
        print(f" (r) register a new player")
        print(f" (s) show the leader board")
        print(f" (p) play a game")
        print(f" (q) quit")

    def register_new_player(self):
        print(f"{Player.check_player_exist('test')}")

    def game_menu(self):
        print("\nWhich game would you like to play?")
        print(" (o) Odd-or-Even")
        print(" (m) Maxi")
        print(" (b) Bunc")

def main()
    cli1 = CommandLineInterface()
    player1 = Player()
    cli1.display_greeting()
    game1 = Game(player1)
    dice1 = Dice()
    dice2 = Dice()
    dice3 = Dice()

    user_input = input(cli1.display_main_menu())
    while user_input.lower() != "q":
        if user_input.lower() == "r":
            playerName = input("What is the name of the new player?\n>")
            if player1.add_player(playerName) == True:
                print(f"Welcome, {playerName}!")
            else:
                print("Sorry, the name is already taken.")
        elif user_input.lower() == "p":
                choose_game = "x"
                while choose_game.lower() not in game1.GAMELIST:
                    cli1.game_menu()
                    choose_game = input("> ")
                print(f"choose game: {choose_game.lower()}")
                if choose_game.lower() == "o":
                    ooe = OddOrEven(game1, dice1)
                    ooe.play_game()
                elif choose_game.lower() == "m":
                    
                    if player1.reg_player_count() > 2:
                        maxi1 = Maxi(game1, dice1, dice2)
                        maxi1.play_game()
                    else:
                        print(f"Not enough players to play Maxi")
                else:
                    if player1.reg_player_count() > 1:
                        bunco1 = Bunco(game1, dice1, dice2, dice3)
                        bunco1.play_game()

        else:
            print("exist from else")


if __name__ == "__main__":
    main()