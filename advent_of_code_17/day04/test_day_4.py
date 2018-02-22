import unittest
import day04.day_4 as day


class TestDay41(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(1, day.Day41("aa bb cc dd ee").get_result())

    def test_example_2(self):
        self.assertEqual(0, day.Day41("aa bb cc dd aa").get_result())

    def test_example_3(self):
        self.assertEqual(1, day.Day41("aa bb cc dd aaa").get_result())

    def test_final_result(self):
        input_content = open("input_4", 'r').read()
        print(day.Day41(input_content).get_result())


class TestDay42(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(1, day.Day42("abcde fghij").get_result())

    def test_example_2(self):
        self.assertEqual(0, day.Day42("abcde xyz ecdab").get_result())

    def test_example_3(self):
        self.assertEqual(1, day.Day42("a ab abc abd abf abj").get_result())

    def test_example_4(self):
        self.assertEqual(1, day.Day42("iiii oiii ooii oooi oooo").get_result())

    def test_example_5(self):
        self.assertEqual(0, day.Day42("oiii ioii iioi iiio").get_result())

    def test_final_result(self):
        input_content = open("input_4", 'r').read()
        print(day.Day42(input_content).get_result())
