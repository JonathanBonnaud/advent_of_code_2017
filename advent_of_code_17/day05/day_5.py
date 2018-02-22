"""
Day 5: A Maze of Twisty Trampolines, All Alike
"""
import abstract_day


class Day51(abstract_day.AbstractDay):

    def get_result(self):
        """
        :return: Number of steps to reach the exit.
        """
        list_digits = self.input_content.split('\n')
        list_digits = [int(i) for i in list_digits]
        pos = 0
        steps = 0
        while pos < len(list_digits):
            steps += 1
            last_pos = pos
            pos += list_digits[pos]
            list_digits[last_pos] += 1
        return steps


class Day52(abstract_day.AbstractDay):

    def get_result(self):
        """
        :return: Number of steps to reach the exit.
        """
        list_digits = self.input_content.split('\n')
        list_digits = [int(i) for i in list_digits]
        pos = 0
        steps = 0
        while -1 < pos < len(list_digits):
            steps += 1
            last_pos = pos
            # print(pos)
            # print(list_digits)
            pos += list_digits[pos]
            if list_digits[last_pos] < 3:
                list_digits[last_pos] += 1
            else:
                list_digits[last_pos] -= 1
        return steps
