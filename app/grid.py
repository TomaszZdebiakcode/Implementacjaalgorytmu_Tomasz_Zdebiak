import random


class Grid:
    def __init__(self, width, height, obstacle_prob=0.2):
        self.width = width
        self.height = height

        self.grid = [
            [
                1 if random.random() < obstacle_prob else 0
                for _ in range(width)
            ]
            for _ in range(height)
        ]

    def is_valid(self, x, y):
        return (
            0 <= x < self.width
            and 0 <= y < self.height
            and self.grid[y][x] == 0
        )

    def neighbors(self, x, y):

        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]

        result = []

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if self.is_valid(nx, ny):
                result.append((nx, ny))

        return result