import unittest
import day05.day_5 as day


class TestDay51(unittest.TestCase):

    def test_example_1(self):
        input_content = "0\n3\n0\n1\n-3"
        self.assertEqual(5, day.Day51(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_5", 'r').read()
        print(day.Day51(input_content).get_result())


class TestDay52(unittest.TestCase):

    def test_example_1(self):
        input_content = "0\n3\n0\n1\n-3"
        self.assertEqual(10, day.Day52(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_5", 'r').read()
        print(day.Day52(input_content).get_result())
