#
# File: GameOddOrEven.py
# Description: Setup an odd or even boardgame class.
# Author: Arun Sharma
# Student ID: 110353025
# Email ID: shaay177
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

from Game import Game

class Bunco:

    def __init__(self, game, dice1, dice2, dice3):
        # assign game and dice object to the Maxi
        self._game = game
        self._dice1 = dice1
        self._dice2 = dice2
        self._dice3 = dice3
        self._round = dict()

    def play_game(self):
        self._game.select_num_player(2, 4)
        self._game.add_player()
        print("Let the game begin")
        self.start_bunco()
    
    def create_point_list(self):
        for p in self._game.player:
            self._round[p] = []
    
    def update_player_list(self, lastPlayer):
        count = 0
        startPoint = 0
        lastPlayerPoint = 0
        countPlayer = len(self._game.player)
        emptyPlayerLst = list()
        for p in self._game.player:
            if p == lastPlayer:
                if count < countPlayer - 1:
                    startPoint = count + 1
                else:
                    startPoint = 0
                lastPlayerPoint = count
            count += 1
        
        count = 0
        
        if startPoint > 0:
            initialSP = startPoint
            while startPoint < countPlayer:
                emptyPlayerLst.append(self._game.player[startPoint])
                startPoint += 1
            while count < startPoint:
                emptyPlayerLst.append(self._game.player[count])
                count += 1
        else:
            while startPoint < countPlayer:
                emptyPlayerLst.append(self._game.player[startPoint])
                startPoint += 1
        
        self._game.player = list()
        for p in emptyPlayerLst:
            self._game.player.append(p)


    def start_bunco(self):
        self.create_point_list()
        loop = 1
        lastPlayer = None
        while loop < 7:        
            for p in self._game.player:
                point = 1
                rPoint = 0
                lastPlayer = p
                while point != 0:
                    print(f"It's {p}'s turn.")
                    self._dice1.throw_dice()
                    self._dice1.generate_throw_strength()
                    self._dice2.throw_dice()
                    s1 = self._dice1.get_diceValue
                    t1 = self._dice1.throwStrength
                    self._dice2.set_throwStrength(t1)
                    self._dice3.set_throwStrength(t1)
                    print(f"{self._dice1.get_dice_face()} {self._dice2.get_dice_face()} {self._dice3.get_dice_face()}")
                    point = self.bunco_points(self._dice1.get_dice_wg_throw_vlaue(),
                                self._dice2.get_dice_wg_throw_vlaue(),
                                self._dice3.get_dice_wg_throw_vlaue(), loop)
                    rPoint += point
                    if rPoint >= 21:
                        point = 0
                if rPoint >= 21:
                    self._round[p].append(rPoint)
                    self._game[p].set_buncos()
                    self._game[p].set_games_won()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                    self.update_player_list(lastPlayer)
                    print(f"{p} is the winner of round {loop}")
                    break
                else:
                    self._round[p].append(rPoint)

            loop += 1

    
    def bunco_points(self, dv1, dv2, dv3, round):
        print(f"dv1 {dv1}, dv2 {dv2}, dv3 {dv3}, round {round}  ")
        point = 0
        if dv1 == dv2 == dv3 == round:
            point = 21
        elif dv1 == dv2 == dv3 != round:
            point = 5
        elif dv1 == round:
            point += 1
        elif dv2 == round:
            point += 1
        elif dv3 == round:
            point += 1
        return point