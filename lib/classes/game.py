class Game:
    def __init__(self, title):
        if type(title) is not str or len(title) < 1:
            raise Exception("Title must be a string of length greater than 0.")
        self._title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        raise Exception("Title cannot be changed after the Game is initialized")

    def results(self, new_result=None):
        if new_result:
            self._results.append(new_result)
        return self._results

    def players(self, new_player=None):
        if new_player:
            self._players.append(new_player)
        return self._players

    def average_score(self, player):
        scores = [result.score for result in self._results if result.player == player]
        return sum(scores) / len(scores) if scores else 0
