import unittest
import day06.day_6 as day


class TestDay61(unittest.TestCase):

    def test_example_1(self):
        input_content = "0	2	7	0"
        self.assertEqual(5, day.Day61(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_6", 'r').read()
        print(day.Day61(input_content).get_result())


class TestDay62(unittest.TestCase):

    def test_example_1(self):
        input_content = "0	2	7	0"
        self.assertEqual(4, day.Day62(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_6", 'r').read()
        print(day.Day62(input_content).get_result())
