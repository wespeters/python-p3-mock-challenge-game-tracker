from .player import Player
from .game import Game

class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise Exception("Player must be an instance of Player class.")
        if not isinstance(game, Game):
            raise Exception("Game must be an instance of Game class.")
        if not(1 <= score <= 5000):
            raise Exception("Score must be an integer between 1 and 5000, inclusive.")
        self._player = player
        self._game = game
        self._score = score
        self.all.append(self)
        player.results(self)
        player.games_played(game)
        game.results(self)
        game.players(player)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not(1 <= score <= 5000):
            raise Exception("Score must be an integer between 1 and 5000, inclusive.")
        self._score = score

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if not isinstance(player, Player):
            raise Exception("Player must be an instance of Player class.")
        self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if not isinstance(game, Game):
            raise Exception("Game must be an instance of Game class.")
        self._game = game
