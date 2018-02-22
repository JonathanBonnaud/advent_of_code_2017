import unittest
import day10.day_10 as day


class TestDay101(unittest.TestCase):

    def test_example_1(self):
        input_content = "3, 4, 1, 5"
        self.assertEqual(12, day.Day101(input_content, test=True).get_result())

    def test_final_result(self):
        input_content = open("input_10", 'r').read()
        print(day.Day101(input_content).get_result())  # 40132


class TestDay102(unittest.TestCase):

    def test_knot_hash_empty_string(self):
        input_content = ""
        self.assertEqual("a2582a3a0e66e6e86e3812dcb672a272", day.Day102(input_content).get_result())

    def test_knot_hash_example_1(self):
        input_content = "AoC 2017"
        self.assertEqual("33efeb34ea91902bb2f59c9920caa6cd", day.Day102(input_content).get_result())

    def test_knot_hash_example_2(self):
        input_content = "1,2,3"
        self.assertEqual("3efbe78a8d82f29979031a4aa0b16a9d", day.Day102(input_content).get_result())

    def test_knot_hash_example_3(self):
        input_content = "1,2,4"
        self.assertEqual("63960835bcdc130f0b66d7ff4f6a5a8e", day.Day102(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_10", 'r').read()
        print(day.Day102(input_content).get_result())  # 35b028fe2c958793f7d5a61d07a008c8
