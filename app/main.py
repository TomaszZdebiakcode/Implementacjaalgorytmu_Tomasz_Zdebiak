from astar import astar
from grid import Grid
from visualization import draw_grid

def main():

    grid = Grid(20, 20, obstacle_prob=0.2)

    start = (0, 0)
    goal = (19, 19)

    grid.grid[0][0] = 0
    grid.grid[19][19] = 0

    result = astar(grid, start, goal)

    if result:

        print("Path found!")
        print("Visited nodes:", result["visited"])
        print("Path length:", len(result["path"]))

        draw_grid(grid, result["path"])

    else:
        print("No path found")


if __name__ == "__main__":
    main()