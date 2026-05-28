from astar import astar
from bfs import bfs
from grid import Grid
from visualization import draw_grid

import time


def main():

    grid = Grid(20, 20, obstacle_prob=0.05)

    start = (0, 0)
    goal = (19, 19)

    grid.grid[0][0] = 0
    grid.grid[19][19] = 0

    t1 = time.perf_counter()
    result_a = astar(grid, start, goal)
    t2 = time.perf_counter()

    t3 = time.perf_counter()
    result_b = bfs(grid, start, goal)
    t4 = time.perf_counter()

    if result_a and result_b:

        print("=== A* ===")
        print("Visited nodes:", result_a["visited"])
        print("Path length:", len(result_a["path"]))
        print("Time:", t2 - t1)

        print()

        print("=== BFS ===")
        print("Visited nodes:", result_b["visited"])
        print("Path length:", len(result_b["path"]))
        print("Time:", t4 - t3)

        draw_grid(grid, result_a["path"])

    else:
        print("No path found")


if __name__ == "__main__":
    main()