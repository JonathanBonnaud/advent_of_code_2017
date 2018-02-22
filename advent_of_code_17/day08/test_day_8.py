import unittest
import day08.day_8 as day


class TestDay81(unittest.TestCase):

    def test_example_1(self):
        input_content = open("test_example_1", 'r').read()
        self.assertEqual(1, day.Day81(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_8", 'r').read()
        print(day.Day81(input_content).get_result())


class TestDay82(unittest.TestCase):

    def test_example_1(self):
        input_content = open("test_example_1", 'r').read()
        self.assertEqual(10, day.Day82(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_8", 'r').read()
        print(day.Day82(input_content).get_result())
