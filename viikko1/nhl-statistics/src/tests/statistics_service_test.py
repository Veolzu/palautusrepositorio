import unittest
from player import Player
from statistics_service import StatisticsService, SortBy



class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_searching_hello(self):
        self.assertEqual("Hello world", "Hello world")

    def test_searching_real_player(self):
        player = self.stats.search("Kurri")
        self.assertIsInstance(player, Player)
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)
        self.assertEqual(player.points, 90)    # ...

    def test_searching_fake_player(self):
        player = self.stats.search("Veeti")
        self.assertIsNone(player)

    def test_team(self):
        team = self.stats.team("EDM")
        actual = [
            (player.name, player.team, player.goals, player.assists)
            for player in team
        ]
        expected = [
            ("Semenko", "EDM", 4, 12),
            ("Kurri", "EDM", 37, 53),
            ("Gretzky", "EDM", 35, 89),
        ]

        self.assertEqual(actual, expected)

    def test_top_points(self):
        player = self.stats.top(1, SortBy.POINTS)
        actual = [
            (player.name, player.team, player.goals, player.assists)
            for player in player
        ]
        expected = [
            ("Gretzky", "EDM", 35, 89)
        ]
        self.assertEqual(actual, expected)
    def test_top_assist(self):
        player = self.stats.top(1, SortBy.ASSISTS)
        actual = [
            (player.name, player.team, player.goals, player.assists)
            for player in player
        ]   
        expected = [
            ("Gretzky", "EDM", 35, 89)
        ]
        self.assertEqual(actual, expected)

    def test_top_goals(self):
        player = self.stats.top(1, SortBy.GOALS)
        actual = [
            (player.name, player.team, player.goals, player.assists)
            for player in player
        ]   
        expected = [
            ("Lemieux", "PIT", 45, 54)
        ]
        self.assertEqual(actual, expected)