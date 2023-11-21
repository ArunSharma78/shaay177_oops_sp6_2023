class PlayerScore:
    # Create a player score object with default attribute values
    
    def __init__(self, chips = 120, gamesPlayed = 0, gamesWon = 0, buncos = 0):
        self._chips = chips
        self._gamesPlayed = gamesPlayed
        self._gamesWon = gamesWon
        self._buncos = buncos
  
    @property
    def chips(self):
        return self._chips

    @property
    def gamesPlayed(self):
        return self._gamesPlayed
    
    @property
    def gamesWon(self):
        return self._gamesWon
    
    @property
    def buncos(self):
        return self._buncos

    def update_chips(self, chips, addOrSubtract = "add"):
        if addOrSubtract.lower() == "add":
            self._chips = self._chips + chips
        else:
            self._chips = self._chips - chips

    def set_games_played(self, gamesPlayed):
        self._gamesPlayed = gamesPlayed

    def set_games_won(self, gamesWon):
        self._gamesWon = gamesWon

    def set_buncos(self, buncos):
        self._buncos = buncos

