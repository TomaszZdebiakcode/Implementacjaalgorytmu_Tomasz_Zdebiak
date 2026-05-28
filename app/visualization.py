import matplotlib.pyplot as plt
import numpy as np


def draw_grid(grid, path=None):

    data = np.array(grid.grid)

    plt.figure(figsize=(8, 8))

    plt.imshow(data, cmap="binary")

    if path:

        xs = [p[0] for p in path]
        ys = [p[1] for p in path]

        plt.plot(xs, ys)

    plt.show()