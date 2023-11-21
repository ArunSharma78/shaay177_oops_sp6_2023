#
# File: Dice.py
# Description: Dice class to setup dice attributes.
# Author: Arun Sharma
# Student ID: 110353025
# Email ID: shaay177
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

import random

class Dice:
    DICEFACE = {1 : "⚀", 2 : "⚁", 3 : "⚂", 4 : "⚃", 5 : "⚄", 6 : "⚅"}

    def __init__(self):
        self._diceValue = random.randint(1, 6)
        self._throwStrength = 0

    def get_diceValue(self):
        return self._diceValue
        
    @property
    def throwStrength(self):
        return self._throwStrength
    
    def set_throwStrength(self, value):
        self._throwStrength = value
    
    def generate_throw_strength(self):
        while True:
            print("How strong will you throw (0-5)?")
            try:
                value = int(input("> "))
                if value in [0, 1, 2, 3, 4, 5]:
                    break  # Break out of the loop if a valid input is provided
                else:
                    print("Invalid choice. Please enter a number between 0 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        self._throwStrength = value

    def throw_dice(self):
        self._diceValue = random.randint(1, 6)

    def get_dice_wg_throw_vlaue(self):
        value = (self._diceValue + self._throwStrength) % 6 
        if value == 0:
            value = 6   #Since 6 mod 6 is 0 while it should be 6
        return value
    
    def get_dice_face(self):
        print(f"{self.get_dice_wg_throw_vlaue()}")
        return self.DICEFACE[self.get_dice_wg_throw_vlaue()]