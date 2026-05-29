from astar import astar
from bfs import bfs
from grid import Grid

import time


def run_experiment():

    warehouse_sizes = [10, 20, 50]
    shelf_densities = [0.05, 0.1, 0.2]

    for warehouse_size in warehouse_sizes:

        for shelf_density in shelf_densities:

            warehouse = Grid(
                warehouse_size,
                warehouse_size,
                shelf_density,
            )

            robot_position = (0, 0)

            vending_machine = (
                warehouse_size - 1,
                warehouse_size - 1,
            )

            warehouse.grid[0][0] = 0

            warehouse.grid[
                warehouse_size - 1
            ][
                warehouse_size - 1
            ] = 0

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

            print()
            print("================================")
            print(f"Warehouse size: {warehouse_size}x{warehouse_size}")
            print(f"Shelf density: {shelf_density}")

            if result_astar and result_bfs:

                print()
                print("A*")

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
                print("BFS")

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

            else:
                print(
                    "Robot could not reach the vending machine",
                )


if __name__ == "__main__":
    run_experiment()