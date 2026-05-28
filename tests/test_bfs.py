from app.bfs import bfs
from app.grid import Grid


def test_bfs_finds_path():

    grid = Grid(5, 5, obstacle_prob=0)

    start = (0, 0)
    goal = (4, 4)

    result = bfs(grid, start, goal)

    assert result is not None