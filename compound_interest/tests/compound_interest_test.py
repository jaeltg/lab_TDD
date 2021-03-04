import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    # Tests

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_returns_compound_interest__scenario_1(self):
        compound_interest = CompoundInterest(100, 10, 20)
        self.assertEqual(732.81, compound_interest.calculate_final_investment())

    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_returns_compound_interest__scenario_2(self):
        compound_interest = CompoundInterest(100, 6, 10)
        self.assertEqual(181.94, compound_interest.calculate_final_investment())

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_returns_compound_interest__scenario_3(self):
        compound_interest = CompoundInterest(100000, 5, 8)
        self.assertEqual(149,058.55, compound_interest.calculate_final_investment())

    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_returns_compound_interest__scenario_4(self):
        compound_interest = CompoundInterest(0, 10, 1)
        self.assertEqual(0.00, compound_interest.calculate_final_investment())

    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_returns_compound_interest__scenario_5(self):
        compound_interest = CompoundInterest(100, 0, 10)
        self.assertEqual(100.00, compound_interest.calculate_final_investment())


    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

