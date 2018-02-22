import unittest
import day01.day_1 as day


class TestDay11(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(3, day.Day11("1122").get_result())

    def test_example_2(self):
        self.assertEqual(4, day.Day11("1111").get_result())

    def test_example_3(self):
        self.assertEqual(0, day.Day11("1234").get_result())

    def test_example_4(self):
        self.assertEqual(9, day.Day11("91212129").get_result())

    def test_final_result(self):
        input_content = open("input_1", 'r').read()
        print(day.Day11(input_content).get_result())


class TestDay12(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(6, day.Day12("1212").get_result())

    def test_example_2(self):
        self.assertEqual(0, day.Day12("1221").get_result())

    def test_example_3(self):
        self.assertEqual(4, day.Day12("123425").get_result())

    def test_example_4(self):
        self.assertEqual(12, day.Day12("123123").get_result())

    def test_example_5(self):
        self.assertEqual(4, day.Day12("12131415").get_result())

    def test_final_result(self):
        input_content = open("input_1", 'r').read()
        print(day.Day12(input_content).get_result())
