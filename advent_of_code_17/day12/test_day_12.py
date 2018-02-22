import unittest
import day12.day_12 as day


class TestDay121(unittest.TestCase):

    def test_example_1(self):
        input_content = open("example_1", 'r').read()
        self.assertEqual(6, len(day.Day121(input_content).get_result()))

    def test_example_2(self):
        input_content = open("example_2", 'r').read()
        self.assertEqual(6, len(day.Day121(input_content).get_result()))

    def test_final_result(self):
        input_content = open("input_12", 'r').read()
        print(len(day.Day121(input_content).get_result()))  # 288


class TestDay122(unittest.TestCase):

    def test_example_1(self):
        input_content = open("example_1", 'r').read()
        self.assertEqual(2, len(day.Day121(input_content, get_groups=True).get_result()))

    def test_final_result(self):
        input_content = open("input_12", 'r').read()
        print(len(day.Day121(input_content, get_groups=True).get_result()))  # 211
