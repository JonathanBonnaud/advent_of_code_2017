"""
Day 9: Stream Processing
"""
import abstract_day


OPEN_GARBAGE = '<',
CLOSE_GARBAGE = '>',
IGNORE = '!',
OPEN_GROUP = '{',
CLOSE_GROUP = '}'


class Stack:
    """Stack implementation with a list"""

    def __init__(self):
        self.stack = ['BEGIN']

    def __str__(self):
        r = '['
        for element in self.stack:
            r += element + '|'
        return r + ']'

    def __len__(self):
        return len(self.stack)

    def get_top(self):
        """Return the element at the top"""
        try:
            return self.stack[-1]
        except Exception as e:
            print("Error:", e)

    def push(self, element):
        """Add an element to the top of the stack (Push)"""
        return self.stack.append(element)

    def pop(self):
        """Remove the element at the top (Pop)"""
        try:
            return self.stack.pop()
        except Exception as e:
            print("Error:", e)


class Day91(abstract_day.AbstractDay):

    @staticmethod
    def get_score(stack):
        return len(stack)

    def get_result(self):
        """
        :return: The number of groups in the stream.
        """
        score, pos = 0, 0
        stack_automaton = Stack()
        while pos < len(self.input_content):
            current_char = self.input_content[pos]
            if not stack_automaton.get_top() in OPEN_GARBAGE:
                if current_char in OPEN_GARBAGE:
                    stack_automaton.push(current_char)
                if current_char in OPEN_GROUP:
                    stack_automaton.push(current_char)
                elif current_char in CLOSE_GROUP:
                    stack_automaton.pop()
                    score += self.get_score(stack_automaton)
            elif current_char in CLOSE_GARBAGE:
                stack_automaton.pop()
            pos = pos+2 if current_char in IGNORE else pos+1
            # print(stack_automaton)
        return score


class Day92(abstract_day.AbstractDay):

    def get_result(self):
        """
        :return: The number of characters in the garbage.
        """
        garbage_counter, pos = 0, 0
        stack_automaton = Stack()
        while pos < len(self.input_content):
            current_char = self.input_content[pos]
            if not stack_automaton.get_top() in OPEN_GARBAGE:
                if current_char in OPEN_GARBAGE:
                    stack_automaton.push(current_char)
            elif current_char in CLOSE_GARBAGE:
                stack_automaton.pop()
            elif current_char not in IGNORE:
                garbage_counter += 1
            pos = pos+2 if current_char in IGNORE else pos+1
        return garbage_counter
