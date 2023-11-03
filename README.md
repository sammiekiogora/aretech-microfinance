import unittest
from your_application_module import calculate_simple_interest

class TestSimpleInterestCalculator(unittest.TestCase):

    def test_interest_calculation(self):
        principal = 1000
        rate = 5
        time = 2
        interest = calculate_simple_interest(principal, rate, time)
        self.assertEqual(interest, 100.0)

if __name__ == '__main__':
    unittest.main()
