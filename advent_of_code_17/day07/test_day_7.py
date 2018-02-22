import unittest
import day07.day_7 as day


class TestDay71(unittest.TestCase):

    def test_example_1(self):
        input_content = open("test_example_1", 'r').read()
        self.assertEqual("tknk", day.Day71(input_content).get_result().label)

    def test_final_result(self):
        input_content = open("input_7", 'r').read()
        print(day.Day71(input_content).get_result().label)


class TestDay72(unittest.TestCase):

    def test_example_1(self):
        input_content = open("test_example_1", 'r').read()
        self.assertEqual(60, day.Day72(input_content).get_result())

    def test_example_2(self):
        input_content = open("test_example_2", 'r').read()
        self.assertEqual(25, day.Day72(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_7", 'r').read()
        print(day.Day72(input_content).get_result())
