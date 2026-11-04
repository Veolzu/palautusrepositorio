import requests
from rich.console import Console
from rich.text import Text

class Player:
    def __init__(self, _dict):

        self.name = _dict['name']
        self.nationality = _dict['nationality']
        self.assists = _dict['assists']
        self.goals = _dict['goals']
        self. team = _dict['team']
        self.games = _dict['games']
    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals:2} + {self.assists:2} = {self.goals + self.assists:2}"

    def dummy2(self):
        pass
class PlayerReader:
    def __init__(self, url):
        self.response = None
        self.get_response(url)


    def get_response(self, url):
        try:
            self.response = requests.get(url, timeout=10).json()
        except requests.exceptions.Timeout:
            print("Timed out")
    def get_players(self):
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)

        return players


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()
    def dummy(self):
        pass

    def top_scorers_by_nationality(self, nationality):
        Console().print(Text("Players from " + nationality + ":", style="bold cyan"))
        players = [player for player in self.players if player.nationality == nationality]
        players = sorted(players, key= lambda player: (player.goals + player.assists), reverse=True)

        return players
    def top_players_by_team(self, team):
        """Palauttaa listan joukkueen pelaajista pisteiden (goals + assists) mukaan laskevassa järjestyksessä."""
        Console().print(Text("Players from team " + team + ":", style="bold cyan"))
        players = [player for player in self.players if player.team == team]
        players = sorted(players, key=lambda player: (player.goals + player.assists), reverse=True)

        return players
    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        Console().print(Text(f"Top {how_many} goal scorers:", style="bold cyan"))

        players = sorted(self.players, key=lambda player: player.goals, reverse=True)

        return players[:how_many]
