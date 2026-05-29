from astar import astar
from bfs import bfs
from grid import Grid
from visualization import draw_grid

import time


def main():

    warehouse = Grid(20, 20, obstacle_prob=0.05)

    robot_position = (0, 0)
    vending_machine = (19, 19)

    warehouse.grid[0][0] = 0
    warehouse.grid[19][19] = 0

    t1 = time.perf_counter()
    result_astar = astar(
        warehouse,
        robot_position,
        vending_machine,
    )
    t2 = time.perf_counter()

    t3 = time.perf_counter()
    result_bfs = bfs(
        warehouse,
        robot_position,
        vending_machine,
    )
    t4 = time.perf_counter()

    if result_astar and result_bfs:

        print("=== A* ===")
        print(
            "Visited locations:",
            result_astar["visited"],
        )
        print(
            "Route length:",
            len(result_astar["path"]),
        )
        print(
            "Execution time:",
            t2 - t1,
        )

        print()

        print("=== BFS ===")
        print(
            "Visited locations:",
            result_bfs["visited"],
        )
        print(
            "Route length:",
            len(result_bfs["path"]),
        )
        print(
            "Execution time:",
            t4 - t3,
        )

        print()
        print("Route to vending machine found!")

        draw_grid(
            warehouse,
            result_astar["path"],
        )

    else:
        print(
            "Robot could not reach the vending machine",
        )


if __name__ == "__main__":
    main()