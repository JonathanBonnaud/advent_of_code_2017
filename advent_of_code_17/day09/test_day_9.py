import unittest
import day09.day_9 as day


class TestDay91(unittest.TestCase):

    def test_example_1(self):
        input_content = "{}"
        self.assertEqual(1, day.Day91(input_content).get_result())

    def test_example_2(self):
        input_content = "{{{}}}"
        self.assertEqual(6, day.Day91(input_content).get_result())

    def test_example_3(self):
        input_content = "{{},{}}"
        self.assertEqual(5, day.Day91(input_content).get_result())

    def test_example_4(self):
        input_content = "{{{},{},{{}}}}"
        self.assertEqual(16, day.Day91(input_content).get_result())

    def test_example_5(self):
        input_content = "{<{},{},{{}}>}"
        self.assertEqual(1, day.Day91(input_content).get_result())

    def test_example_6(self):
        input_content = "{<a>,<a>,<a>,<a>}"
        self.assertEqual(1, day.Day91(input_content).get_result())

    def test_example_7(self):
        input_content = "{{<a>},{<a>},{<a>},{<a>}}"
        self.assertEqual(9, day.Day91(input_content).get_result())

    def test_example_8(self):
        input_content = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
        self.assertEqual(9, day.Day91(input_content).get_result())

    def test_example_9(self):
        input_content = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
        self.assertEqual(3, day.Day91(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_9", 'r').read()
        print(day.Day91(input_content).get_result())


class TestDay92(unittest.TestCase):

    def test_example_1(self):
        input_content = "{}"
        self.assertEqual(0, day.Day92(input_content).get_result())

    def test_example_5(self):
        input_content = "{<{},{},{{}}>}"
        self.assertEqual(10, day.Day92(input_content).get_result())

    def test_example_6(self):
        input_content = "{<a>,<a>,<a>,<a>}"
        self.assertEqual(4, day.Day92(input_content).get_result())

    def test_example_7(self):
        input_content = "{{<a>},{<a>},{<a>},{<a>}}"
        self.assertEqual(4, day.Day92(input_content).get_result())

    def test_example_8(self):
        input_content = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
        self.assertEqual(0, day.Day92(input_content).get_result())

    def test_example_9(self):
        input_content = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
        self.assertEqual(17, day.Day92(input_content).get_result())

    def test_final_result(self):
        input_content = open("input_9", 'r').read()
        print(day.Day92(input_content).get_result())
