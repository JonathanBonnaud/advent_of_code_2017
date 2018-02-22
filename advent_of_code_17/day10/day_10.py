"""
Day 10: Knot Hash
"""
import abstract_day
import operator
import functools


class Day101(abstract_day.AbstractDay):

    def __init__(self, input_content, *, test=None):
        super().__init__(input_content)
        self.length = 256 if test is None else 5
        self.circular_list = [i for i in range(self.length)]

    def update_circular_list(self, input_lengths, *, skip=0, pos=0):
        skip_size = skip
        current_pos = pos
        for current_length in input_lengths:
            # get sub_list and reverse
            if current_pos + current_length < self.length:
                sub_list_pos = [i for i in range(current_pos, current_pos + current_length)]
            else:
                sub_list_pos = [i for i in range(current_pos, self.length)]
                sub_list_pos.extend([i for i in range(current_length - (self.length - current_pos))])
            sub_list = [self.circular_list[i] for i in sub_list_pos]
            sub_list.reverse()

            # update circular list
            for i, elem in zip(sub_list_pos, sub_list):
                self.circular_list.pop(i)
                self.circular_list.insert(i, elem)

            current_pos = (current_pos + current_length + skip_size) % self.length
            skip_size += 1

        return [skip_size, current_pos]

    def get_result(self):
        """
        From a list of lengths, update the values of a standard list (of size 256)
        by reversing each sublist.
        :return: the multiplication of the two first values in the final list.
        """
        input_lengths = [int(elem.strip()) for elem in self.input_content.split(',')]
        self.update_circular_list(input_lengths)

        res = self.circular_list[0] * self.circular_list[1]
        return res


class Day102(abstract_day.AbstractDay):

    def __init__(self, input_content, *, to_ascii=None):
        super().__init__(input_content)
        self.to_ascii = True if to_ascii is None else to_ascii

    def get_result(self):
        input_lengths = [char for char in self.input_content]

        # - convert list of length to their ascii
        input_lengths = [ord(char) for char in input_lengths]

        # - add to the input lengths : 17, 31, 73, 47, 23
        input_lengths.extend([17, 31, 73, 47, 23])

        # - run 64 times update_circular_list (this will get the list of numbers : the sparse hash
        knot_hash_algo = Day101(input_lengths)
        prev = [0, 0]
        for i in range(64):
            prev = knot_hash_algo.update_circular_list(input_lengths, skip=prev[0], pos=prev[1])

        # - reduce to a list of 16 numbers (called dense hash) : use XOR to combine consecutive lists of 16 numbers
        #   (16 blocks dans list de 256 numbers) ==> 65 ^ 27 ^ ...
        dense_hash = list()
        for i in range(16):
            dense_hash.append(functools.reduce(operator.xor, knot_hash_algo.circular_list[i*16:i*16+16]))

        # - dense hash to hexadecimal string (32 hexadecimal digits (0-f) long)
        knot_hash = ''.join(['{:02x}'.format(elem, 'x') for elem in dense_hash])
        return knot_hash
