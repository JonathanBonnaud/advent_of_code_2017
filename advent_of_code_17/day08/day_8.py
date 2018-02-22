"""
Day 8: I Heard You Like Registers
"""
import abstract_day
import operator
import re
from collections import defaultdict


class Inst:
    REG = 0
    ACTION = 1
    VAL = 2
    COND_REG = 3
    COND_COMP = 4
    COND_VAL = 5


class Day81(abstract_day.AbstractDay):

    def get_result(self):
        """
        :return: The largest value in any register at the end.
        """
        lines = self.input_content.split('\n')
        registers = dict()
        registers = defaultdict(lambda: 0, registers)
        for line in lines:
            instruction = re.search('(\w+) (inc|dec) (-?\d+) if (\w+) (..?) (-?\d+)', line).groups()
            condition = str(registers[instruction[Inst.COND_REG]]) + str(instruction[Inst.COND_COMP]) +\
                str(instruction[Inst.COND_VAL])
            if eval(condition):
                if instruction[Inst.ACTION] == 'inc':
                    registers[instruction[Inst.REG]] += eval(instruction[Inst.VAL])
                else:
                    registers[instruction[Inst.REG]] -= eval(instruction[Inst.VAL])
        # return max(registers.items(), key=operator.itemgetter(1))[0]
        return max(registers.values())


class Day82(abstract_day.AbstractDay):

    def get_result(self):
        """
        :return: The highest value held in any register during the process.
        """
        lines = self.input_content.split('\n')
        registers = dict()
        registers = defaultdict(lambda: 0, registers)
        max = 0
        for line in lines:
            instruction = re.search('(\w+) (inc|dec) (-?\d+) if (\w+) (..?) (-?\d+)', line).groups()
            condition = str(registers[instruction[Inst.COND_REG]]) + str(instruction[Inst.COND_COMP]) +\
                str(instruction[Inst.COND_VAL])
            if eval(condition):
                if instruction[Inst.ACTION] == 'inc':
                    registers[instruction[Inst.REG]] += eval(instruction[Inst.VAL])
                else:
                    registers[instruction[Inst.REG]] -= eval(instruction[Inst.VAL])
                if registers[instruction[Inst.REG]] > max:
                    max = registers[instruction[Inst.REG]]
        return max
