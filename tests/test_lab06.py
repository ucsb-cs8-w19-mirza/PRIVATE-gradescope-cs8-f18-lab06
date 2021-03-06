import unittest
import pytest
from gradescope_utils.autograder_utils.decorators import weight
import io
from contextlib import redirect_stdout

from lab06 import *


class TestConversion(unittest.TestCase):

    def setUp(self):
        pass

    @weight(10)
    def test_totalWords1(self):
        """Testing totalWords("input1.txt")"""
        assert totalWords("input1.txt") == 104

    @weight(10)
    def test_totalWords2(self):
        """Testing totalWords("input2.txt")"""
        assert totalWords("input2.txt") == 170

    ####################

    @weight(10)
    def test_longestWord1(self):
        """Testing longestWord("input1.txt")"""
        assert longestWord("input1.txt") == "traditional"

    @weight(10)
    def test_longestWord2(self):
        """Testing longestWord("input2.txt")"""
        assert longestWord("input2.txt") == "responsible"

    ####################

    @weight(10)
    def test_charactersPerWord1(self):
        """Testing charactersPerWord("input1.txt")"""
        self.assertEqual(charactersPerWord("input1.txt"), pytest.approx(4.278846153846154))

    @weight(10)
    def test_charactersPerWord2(self):
        """Testing charactersPerWord("input2.txt")"""
        self.assertEqual(charactersPerWord("input2.txt"), pytest.approx(4.3882352941176475))

    ###################

    @weight(10)
    def test_rollDice_multiple(self):
        """Testing rollDice"""
        for i in range(100):
            diceResult = rollDice()
            assert diceResult >= 2 and diceResult <= 12

    ####################
    @weight(10)
    def test_rollDistribution_single(self):
        """Testing the output of rollDistribution"""
        output = rollDistribution(250)

        assert type(output) == list
        assert 13 == len(output)
        assert output[0] == 0
        assert output[1] == 0
        assert 250 == sum(output)

    #####################

    @weight(5)
    def test_printDistribution_format(self):
        """Testing printDistribution output's first and last lines"""

        noOfTimes = 250
        f = io.StringIO()
        with redirect_stdout(f):
            printDistribution(rollDistribution(noOfTimes))
        s = f.getvalue()
        lines = s.strip().split('\n')
        assert lines[0] == "Distribution of dice rolls"
        assert lines[-1] == str(noOfTimes) + " rolls"
        assert lines[-2] == "------------------------------"
        # Making sure only dice values from 2 to 12 is printed
        for i in range(2, 13):
            assert i == int(lines[i].split(':')[0])

    @weight(10)
    def test_printDistribution_asteriskValues(self):
        """Testing printDistribution asterisk output"""
        noOfTimes = 250
        f = io.StringIO()
        with redirect_stdout(f):
            printDistribution(rollDistribution(noOfTimes))
        s = f.getvalue()
        lines = s.strip().split('\n')
        for i in range(2, 13):
            split = lines[i].split(':')[1].strip().split()
            num = int(split[0])
            stars = len(split[-1])
            assert num == stars

    @weight(5)
    def test_printDistribution_percentValues(self):
        """Testing printDistribution percent output"""
        noOfTimes = 250
        f = io.StringIO()
        with redirect_stdout(f):
            printDistribution(rollDistribution(noOfTimes))
        s = f.getvalue()
        lines = s.strip().split('\n')
        for i in range(2, 13):
            split = lines[i].split(':')[1].strip().split()
            num = int(split[0])
            assert split[2] == "{0:.1f}%)".format(num / noOfTimes * 100)


if __name__ == '__main__':
    import pytest

    pytest.main(["./lab06_tests.py"])
