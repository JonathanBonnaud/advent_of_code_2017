"""
Day 11: Hex Ed
"""
import abstract_day
import operator


class Tuple(tuple):
    def __lt__(self, other):
        return True if self[0] < other[0] and self[1] < other[1] else False

    def __gt__(self, other):
        return True if self[0] > other[0] and self[1] > other[1] else False


class Day111(abstract_day.AbstractDay):

    coordinates = {
        'n': (0, 1),
        'ne': (0.5, 0.5),
        'se': (0.5, -0.5),
        's': (0, -1),
        'sw': (-0.5, -0.5),
        'nw': (-0.5, 0.5)
    }

    def __init__(self, input_content, *, get_max=None):
        super().__init__(input_content)
        self.get_max = False if get_max is None else get_max

    @staticmethod
    def add_tuples(tuple1, tuple2):
        return Tuple(map(operator.add, tuple1, tuple2))

    def get_result(self):
        directions = [self.coordinates[coord] for coord in self.input_content.split(',')]
        dest_point = Tuple((0, 0))
        max_point = Tuple((0, 0))
        for coord in directions:
            dest_point = self.add_tuples(dest_point, (coord[0], coord[1]))
            if abs(dest_point[0])+abs(dest_point[1]) > abs(max_point[0])+abs(max_point[1]):
                max_point = dest_point

        dest_point = max_point if self.get_max else dest_point
        steps = 0
        current = Tuple((0, 0))  # (x, y)
        while current != dest_point:
            if current < dest_point:
                # print('ne')
                current = self.add_tuples(current, self.coordinates['ne'])
            elif current > dest_point:
                # print('sw')
                current = self.add_tuples(current, self.coordinates['sw'])
            elif current[0] < dest_point[0] and current[1] > dest_point[1]:
                # print('se')
                current = self.add_tuples(current, self.coordinates['se'])
            elif current[0] > dest_point[0] and current[1] < dest_point[1]:
                # print('nw')
                current = self.add_tuples(current, self.coordinates['nw'])
            elif current[1] < dest_point[1]:
                # print('n')
                current = self.add_tuples(current, self.coordinates['n'])
            elif current[1] > dest_point[1]:
                # print('s')
                current = self.add_tuples(current, self.coordinates['s'])
            steps += 1
        return steps
