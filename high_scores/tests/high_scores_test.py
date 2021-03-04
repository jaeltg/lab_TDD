import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.scores = [10, 11, 100, 42, 21, 29, 59, 83, 1]

    # Test latest score (the last thing in the list)
    def test_can_get_latest_score(self):
        self.assertEqual(1, latest(self.scores))

    # Test personal best (the highest score in the list)
    def test_find_personal_best_score(self):
        self.assertEqual(100, personal_best(self.scores))

    # Test top three from list of scores
    def test_can_find_top_three(self):
        self.assertEqual([100, 83, 59], personal_top_three(self.scores))
        
    # Test ordered from highest tp lowest
    def test_can_sort_highest_to_lowest(self):
        self.assertEqual([100, 83, 59, 42, 29, 21, 11, 10, 1], sort_scores_highest_to_lowest(self.scores))

    # Test top three when there is a tie
    def test_can_find_top_three_when_tie(self):
        scores = [10, 10, 35, 2, 80]
        self.assertEqual([80, 35, 10, 10], personal_top_three(scores))

    # Test top three when there are less than three
    def test_can_find_top_three_when_only_two_scores(self):
        scores = [10, 28]
        self.assertEqual([28, 10], personal_top_three(scores))

    # Test top three when there is only one
    def test_can_find_top_three_when_only_one_score(self):
        scores = [50]
        self.assertEqual([50], personal_top_three(scores))
    
