import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(came_from, current):

    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()

    return path


def astar(grid, start, goal):

    open_set = []

    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {
        start: 0,
    }

    visited_nodes = 0

    while open_set:

        _, current = heapq.heappop(open_set)

        visited_nodes += 1

        if current == goal:

            return {
                "path": reconstruct_path(came_from, current),
                "visited": visited_nodes,
            }

        for neighbor in grid.neighbors(*current):

            tentative_g = g_score[current] + 1

            if (
                neighbor not in g_score
                or tentative_g < g_score[neighbor]
            ):

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(open_set, (f, neighbor))

    return None