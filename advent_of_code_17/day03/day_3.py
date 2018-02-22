"""
Day 3: Spiral Memory
"""
import abstract_day
import math


class Day31(abstract_day.AbstractDay):
    NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions
    turn_right = {NORTH: E, E: S, S: W, W: NORTH}  # old -> new direction

    def spiral(self, width, height):
        if width < 1 or height < 1:
            raise ValueError
        x, y = width // 2, height // 2  # start near the center
        dx, dy = self.NORTH  # initial direction
        matrix = [[None] * width for _ in range(height)]
        count = 0
        while True:
            count += 1
            matrix[y][x] = count  # visit
            # try to turn right
            new_dx, new_dy = self.turn_right[dx, dy]
            new_x, new_y = x + new_dx, y + new_dy
            if (0 <= new_x < width and 0 <= new_y < height and
                        matrix[new_y][new_x] is None):  # can turn right
                x, y = new_x, new_y
                dx, dy = new_dx, new_dy
            else:  # try to move straight
                x, y = x + dx, y + dy
                if not (0 <= x < width and 0 <= y < height):
                    return matrix  # nowhere to go

    def build_matrix(self):
        if int(self.input_content) == 1:
            return list()
        else:
            n = 1
            while int(self.input_content) > math.pow(2*n+1, 2):
                n += 1
            matrix_size = 2*n+1

            return self.spiral(matrix_size, matrix_size)

    def get_result(self):
        matrix = self.build_matrix()
        if not matrix:
            return 0

        steps = 0
        return steps
