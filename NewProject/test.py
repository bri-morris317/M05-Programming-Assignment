from fractions import Fraction

import unittest

from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result=sum(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()


    #After trying to achieve test results based on the code given I'm not exactly sure what is wrong with my system.
    #I'm using VS Code as my IDE and many of the functions from the instructions don't even exist because the article is at least 4 years old.
    #Testing with the previous examples prior to starting the Unittest section I was able to produce a FAIL test with two errors that were
    #related to the sum not equaling 6. I'm going to assume for this particular unittest example the issue is the same. The sums based on the values
    #do not equal six. In order to make the corrections I would need to go back and correct what the code is asking to be summed.
    