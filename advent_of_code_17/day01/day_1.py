"""
Day 1: Inverse Captcha
"""
import abstract_day


class Day11(abstract_day.AbstractDay):

    def get_result(self):
        prev = 0
        sum = 0
        for i in self.input_content:
            if prev == i:
                sum += int(i)
            prev = i
        # last check

        if prev == self.input_content[0]:
            sum += int(self.input_content[0])
        return sum


class Day12(abstract_day.AbstractDay):

    def __init__(self, input_content):
        super().__init__(input_content)
        self.length = len(input_content)
        self.step_length = int(len(input_content) / 2)

    def get_result(self):
        sum = 0
        for i, digit in enumerate(self.input_content):
            # print("i: %d, digit: %s" % (i, digit))
            j = self.step_length
            # print(j)
            if not i+j >= self.length:
                # print("%s compared with %s" % (digit, self.input_content[i+j]))
                if digit == self.input_content[i+j]:
                    sum += int(digit)
            else:
                if digit == self.input_content[i+j - self.length]:
                    sum += int(digit)
            # print("sum: %d" % sum)
        return sum
