import unittest
import day11.day_11 as day


class TestTuple(unittest.TestCase):

    def test_lt(self):
        tuple1 = day.Tuple((0, 0))
        tuple2 = day.Tuple((1, 1))
        self.assertTrue(tuple1 < tuple2)


class TestDay111(unittest.TestCase):

    def test_example_1(self):
        input_content = "ne,ne,ne"
        self.assertEqual(3, day.Day111(input_content).get_result())

    def test_example_2(self):
        input_content = "ne,ne,sw,sw"
        self.assertEqual(0, day.Day111(input_content).get_result())

    def test_example_3(self):
        input_content = "ne,ne,s,s"
        self.assertEqual(2, day.Day111(input_content).get_result())

    def test_example_4(self):
        input_content = "se,sw,se,sw,sw"
        self.assertEqual(3, day.Day111(input_content).get_result())

    def test_example_against_get_max(self):
        input_content = "sw,sw,s,se,sw,s,ne,ne"
        self.assertEqual(3, day.Day111(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_11", 'r').read()
        print(day.Day111(input_content).get_result())  # 824


class TestDay112(unittest.TestCase):

    def test_example_1(self):
        input_content = "ne,ne,ne,ne,s,s"
        self.assertEqual(4, day.Day111(input_content, get_max=True).get_result())

    def test_example_for_get_max(self):
        input_content = "sw,sw,s,se,sw,s,ne,ne"
        self.assertEqual(5, day.Day111(input_content, get_max=True).get_result())

    def test_final_result(self):
        input_content = open("input_11", 'r').read()
        print(day.Day111(input_content, get_max=True).get_result())  # 1548
