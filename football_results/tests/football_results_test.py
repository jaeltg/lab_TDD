import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def setUp(self):
        self.final_scores = [
            {"home_score": 2,
            "away_score": 0},
             {"home_score": 0,
            "away_score": 3},
             {"home_score": 1,
            "away_score": 1}
        ]
            
    # Test we get the right result string for a final score dictionary representing -
    def test_home_win(self):
        self.assertEqual("Home win", get_result(self.final_scores[0]))

    def test_away_win(self):
        self.assertEqual("Away win", get_result(self.final_scores[1]))

    def test_draw(self):
        self.assertEqual("Draw", get_result(self.final_scores[2]))
        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_list_results(self):
        self.assertEqual(["Home win", "Away win", "Draw"], get_results(self.final_scores))
    # [home win, away win]


if __name__ == "__main__":
    unittest.main()
