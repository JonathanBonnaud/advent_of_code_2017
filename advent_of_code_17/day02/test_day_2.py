import unittest
import day02.day_2 as day


class TestDay21(unittest.TestCase):

    def test_example_1(self):
        test_input = "5	1	9	5\n7	5	3\n2	4	6	8"
        self.assertEqual(18, day.Day21(test_input).get_result())

    def test_final_result(self):
        test_input = open("input_2", 'r').read()
        print(day.Day21(test_input).get_result())


class TestDay22(unittest.TestCase):

    def test_example_1(self):
        test_input = "5	9	2	8\n9	4	7	3\n3	8	6	5"
        self.assertEqual(9, day.Day22(test_input).get_result())

    def test_final_result(self):
        test_input = open("input_2", 'r').read()
        print(day.Day22(test_input).get_result())
