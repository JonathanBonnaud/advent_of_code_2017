import unittest
import day13.day_13 as day


class TestDay131(unittest.TestCase):

    def test_example_1(self):
        input_content = open("example_1", 'r').read()
        self.assertEqual(24, day.Day131(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_13", 'r').read()
        print(day.Day131(input_content).get_result())


class TestDay132(unittest.TestCase):
    pass
