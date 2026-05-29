import matplotlib.pyplot as plt
import numpy as np


def draw_grid(warehouse, path=None):

    data = np.array(warehouse.grid)

    plt.figure(figsize=(10, 10))

    plt.imshow(
        data,
        cmap="Greys",
        origin="upper",
    )

    if path:

        xs = [position[0] for position in path]
        ys = [position[1] for position in path]

        # trasa robota
        plt.plot(
            xs,
            ys,
            linewidth=3,
            label="Robot route",
        )

        # robot (start)
        plt.scatter(
            xs[0],
            ys[0],
            color="green",
            s=250,
            marker="o",
            label="Robot",
        )

        # automat vendingowy (cel)
        plt.scatter(
            xs[-1],
            ys[-1],
            color="red",
            s=300,
            marker="s",
            label="Vending machine",
        )

    plt.title(
        "Warehouse Navigation for Vending Machine Restocking",
        fontsize=14,
    )

    plt.xlabel("Warehouse X position")
    plt.ylabel("Warehouse Y position")

    plt.xticks(range(warehouse.width))
    plt.yticks(range(warehouse.height))

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.show()