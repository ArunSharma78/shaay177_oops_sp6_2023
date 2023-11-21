from PlayerScore import PlayerScore

class Player:

    def __init__(self):
        # An empty player and playerScore is initiated in this class

        self._player = set()
        self._playerScore = dict()
    
    def check_player_exist(self, name):
        # Check if the player already registered in the system

        if name.lower() in self._player:
            return True
        else:
            return False

    def add_player(self, name):
        # Add player in the game if it doesn't exist
        # initialise player score too

        if self.check_player_exist(name):
            return False
        else:
            self._player.add(name.lower())
            self._playerScore[name.lower()] = PlayerScore()
            return True

    def chips(self, name):
        return self._playerScore[name.lower()].chips

    def update_chips(self, name, newChips, addOrSubtract):
        self._playerScore[name.lower()].update_chips(newChips, addOrSubtract)
    
    def games_played(self, name):
        return self._playerScore[name.lower()].gamesPlayed
    
    def games_won(self, name):
        return self._playerScore[name.lower()].gamesWon
    
    def buncos(self, name):
        return self._playerScore[name.lower()].buncos
        


        