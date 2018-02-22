import unittest
import day03.day_3 as day


class TestDay31(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(0, day.Day31("1").get_result())

    def test_example_2(self):
        self.assertEqual(3, day.Day31("12").get_result())

    def test_example_3(self):
        self.assertEqual(2, day.Day31("23").get_result())

    def test_example_4(self):
        self.assertEqual(31, day.Day31("1024").get_result())
