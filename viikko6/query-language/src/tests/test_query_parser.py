import unittest

from player import Player
from query_parser import parse


class QueryParserTest(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player("Alexis Lafrenière", "NYR", 17, 28),
            Player("Jonny Brodzinski", "NYR", 12, 7),
            Player("Adam Fox", "NYR", 10, 51),
            Player("Artemi Panarin", "NYR", 49, 71),
            Player("Connor McDavid", "EDM", 26, 74),
            Player("Low scorer", "EDM", 4, 7),
        ]

    def matching_names(self, query):
        matcher = parse(query)
        return [player.name for player in self.players if matcher.test(player)]

    def test_team_condition(self):
        self.assertEqual(
            self.matching_names("team = NYR"),
            [player.name for player in self.players[:4]],
        )

    def test_numeric_conditions(self):
        self.assertEqual(
            self.matching_names("goals >= 17"),
            ["Alexis Lafrenière", "Artemi Panarin", "Connor McDavid"],
        )
        self.assertEqual(self.matching_names("goals < 10"), ["Low scorer"])

    def test_and_conditions(self):
        self.assertEqual(
            self.matching_names("team = NYR and goals >= 10 and goals < 20"),
            ["Alexis Lafrenière", "Jonny Brodzinski", "Adam Fox"],
        )

    def test_and_binds_more_tightly_than_or(self):
        self.assertEqual(
            self.matching_names("team = NYR and goals >= 17 or goals < 5"),
            ["Alexis Lafrenière", "Artemi Panarin", "Low scorer"],
        )

    def test_not_condition(self):
        self.assertEqual(self.matching_names("not team = NYR"), ["Connor McDavid", "Low scorer"])
        self.assertEqual(
            self.matching_names("not goals >= 10 and team = EDM"),
            ["Low scorer"],
        )

    def test_not_binds_more_tightly_than_and(self):
        self.assertEqual(
            self.matching_names("not team = NYR and goals >= 10 or goals < 5"),
            ["Connor McDavid", "Low scorer"],
        )

    def test_accepts_surrounding_whitespace(self):
        self.assertEqual(self.matching_names("  team = NYR  "), [player.name for player in self.players[:4]])

    def test_rejects_invalid_queries(self):
        for query in (
            "",
            "team NYR",
            "goals = 10",
            "team >= 10",
            "goals < nope",
            "team = NYR xor goals >= 10",
            "team = NYR and",
        ):
            with self.subTest(query=query):
                with self.assertRaises(ValueError):
                    parse(query)


if __name__ == "__main__":
    unittest.main()
