class Player:
    all = []

    def __init__(self, username):
        if type(username) is not str or not(2 <= len(username) <= 16):
            raise Exception("Username must be a string of length between 2 and 16, inclusive.")
        self._username = username
        self._results = []
        self._games_played = []
        self.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if type(username) is not str or not(2 <= len(username) <= 16):
            raise Exception("Username must be a string of length between 2 and 16, inclusive.")
        self._username = username

    def results(self, new_result=None):
        if new_result:
            self._results.append(new_result)
        return self._results

    def games_played(self, new_game=None):
        if new_game:
            self._games_played.append(new_game)
        return self._games_played

    def played_game(self, game):
        return game in self._games_played

    def num_times_played(self, game):
        return sum(1 for result in self._results if result.game == game)

    @classmethod
    def highest_scored(cls, game):
        players = [result.player for result in game.results()]
        if not players:
            return None
        return max(players, key=lambda player: game.average_score(player))
