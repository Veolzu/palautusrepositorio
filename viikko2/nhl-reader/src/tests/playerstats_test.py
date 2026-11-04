# coding: utf-8
import pytest

from player import PlayerStats


class StubReader:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


class DummyPlayer:
    def __init__(self, name, team, nationality, goals, assists, games=0):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
        self.games = games


def make_players():
    return [
        DummyPlayer("A One", "BOS", "USA", 10, 5),
        DummyPlayer("B Two", "BOS", "CAN", 8, 10),
        DummyPlayer("C Three", "NYR", "USA", 15, 0),
        DummyPlayer("D Four", "NYR", "SWE", 7, 7),
        DummyPlayer("E Five", "BOS", "FIN", 10, 10),
    ]


def test_top_goal_scorers_returns_n_players_sorted_by_goals():
    players = make_players()
    reader = StubReader(players)

    stats = PlayerStats(reader)

    top2 = stats.top_goal_scorers(2)

    assert len(top2) == 2
    assert top2[0].name == "C Three"  # 15 goals
    # second should be a 10-goal player
    assert top2[1].goals == 10


def test_top_scorers_by_nationality_filters_and_sorts_by_points():
    players = make_players()
    reader = StubReader(players)
    stats = PlayerStats(reader)

    usa = stats.top_scorers_by_nationality("USA")

    # USA players: A One (10+5=15), C Three (15+0=15) -> order by points (tie allowed)
    assert len(usa) == 2
    assert all(p.nationality == "USA" for p in usa)
    assert usa[0].goals + usa[0].assists >= usa[1].goals + usa[1].assists


def test_top_players_by_team_filters_and_sorts_by_points():
    players = make_players()
    reader = StubReader(players)
    stats = PlayerStats(reader)

    bos = stats.top_players_by_team("BOS")

    # BOS players: A One (15), B Two (18), E Five (20) -> sorted desc by points
    assert [p.name for p in bos] == ["E Five", "B Two", "A One"]
