"""
Day 6: Memory Reallocation
"""
import abstract_day


def get_pos_bank_max_blocks(banks):
    max_blocks, max_pos = int(banks[0]), 0
    for pos, nb_blocks in enumerate(banks[1:]):
        if int(nb_blocks) > max_blocks:
            max_blocks, max_pos = int(nb_blocks), pos + 1
    return max_pos


class Day61(abstract_day.AbstractDay):

    def get_result(self):
        """
        :return: The number of redistribution cycles before a configuration is produced
        that has been seen before.
        """
        banks = [int(i) for i in self.input_content.split('\t')]  # list of banks
        current_banks = '.'.join([str(bank) for bank in banks])  # string representing the banks
        seen_banks = list()
        steps = 0
        while current_banks not in seen_banks:
            seen_banks.append(current_banks)
            # print("cur: ", current_banks)
            # print("seen: ", seen_banks)
            steps += 1
            i = max_pos = get_pos_bank_max_blocks(banks)
            # print("max pos: ", max_pos)
            bank_to_unstack = banks[max_pos]
            banks[max_pos] = 0
            while bank_to_unstack > 0:
                if i < len(banks)-1:
                    i += 1
                    banks[i] += 1
                    bank_to_unstack -= 1
                    # print("pos %d, val %d" % (i, banks[i]))
                else:
                    i = -1
            # print("new banks:", banks)
            current_banks = '.'.join([str(bank) for bank in banks])
        return steps


class Day62(abstract_day.AbstractDay):

    def get_result(self):
        banks = [int(i) for i in self.input_content.split('\t')]  # list of banks
        current_banks = '.'.join([str(bank) for bank in banks])  # string representing the banks
        seen_banks = dict()
        steps = 0
        while current_banks not in seen_banks:
            seen_banks[current_banks] = 0
            seen_banks.update((k, v + 1) for k, v in seen_banks.items())
            steps += 1
            i = max_pos = get_pos_bank_max_blocks(banks)
            bank_to_unstack = banks[max_pos]
            banks[max_pos] = 0
            while bank_to_unstack > 0:
                if i < len(banks)-1:
                    i += 1
                    banks[i] += 1
                    bank_to_unstack -= 1
                else:
                    i = -1
            current_banks = '.'.join([str(bank) for bank in banks])
        return seen_banks[current_banks]
