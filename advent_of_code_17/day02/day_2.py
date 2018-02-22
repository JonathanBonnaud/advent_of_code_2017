"""
Day 2: Corruption Checksum
"""
import abstract_day


class Day21(abstract_day.AbstractDay):

    def get_result(self):
        """
        :return: Checksum for the spreadsheet in the puzzle input.
        """
        rows = self.input_content.split('\n')
        sum = 0
        for row in rows:
            digits = row.split('\t')
            min = int(digits[0])
            max = int(digits[0])
            for digit in digits[1:]:
                if int(digit) < min:
                    min = int(digit)
                if int(digit) > max:
                    max = int(digit)
            sum += max - min
        return sum


class Day22(abstract_day.AbstractDay):

    def get_result(self):
        """
        :return: Checksum for the spreadsheet in the puzzle input.
        """
        rows = self.input_content.split('\n')
        sum = 0
        for row in rows:
            digits = row.split('\t')
            for pos, d in enumerate(digits[:-1]):
                min = int(d)
                max = int(d)
                for digit in digits[pos+1:]:
                    # print("try %d / %d" % (int(digit), min))
                    if int(digit) % min == 0:
                        add_sum = int(digit) / min
                    elif max % int(digit) == 0:
                        add_sum = max / int(digit)
            sum += int(add_sum)
            # print("sum: %d" % sum)
        return sum