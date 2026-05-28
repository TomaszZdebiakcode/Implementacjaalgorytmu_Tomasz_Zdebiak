from astar import astar
from bfs import bfs
from grid import Grid

import time


def run_experiment():

    sizes = [10, 20, 50]
    obstacles = [0.05, 0.1, 0.2]

    for size in sizes:

        for obstacle_prob in obstacles:

            grid = Grid(size, size, obstacle_prob)

            start = (0, 0)
            goal = (size - 1, size - 1)

            grid.grid[0][0] = 0
            grid.grid[size - 1][size - 1] = 0

            t1 = time.perf_counter()
            result_a = astar(grid, start, goal)
            t2 = time.perf_counter()

            t3 = time.perf_counter()
            result_b = bfs(grid, start, goal)
            t4 = time.perf_counter()

            print()
            print("================================")
            print(f"Grid size: {size}x{size}")
            print(f"Obstacle density: {obstacle_prob}")

            if result_a and result_b:

                print()
                print("A*")
                print("Visited:", result_a["visited"])
                print("Path length:", len(result_a["path"]))
                print("Time:", t2 - t1)

                print()
                print("BFS")
                print("Visited:", result_b["visited"])
                print("Path length:", len(result_b["path"]))
                print("Time:", t4 - t3)

            else:
                print("No path found")


if __name__ == "__main__":
    run_experiment()