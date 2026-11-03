import requests
from rich.console import Console
from rich.text import Text

class Player:
    def __init__(self, dict):

        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self. team = dict['team']
        self.games = dict['games']
    
    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals:2} + {self.assists:2} = {self.goals + self.assists:2}"

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_players(self):
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)

        return players


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()


    def top_scorers_by_nationality(self, nationality):
        Console().print(Text("Players from " + nationality + ":", style="bold cyan"))
        players = [player for player in self.players if player.nationality == nationality]
        players = sorted(players, key= lambda player: (player.goals + player.assists), reverse=True)

        return players
