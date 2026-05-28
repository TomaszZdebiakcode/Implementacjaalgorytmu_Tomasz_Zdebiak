from collections import deque


def bfs(grid, start, goal):

    queue = deque([start])

    visited = set()
    visited.add(start)

    parent = {}

    visited_nodes = 0

    while queue:

        current = queue.popleft()

        visited_nodes += 1

        if current == goal:

            path = []

            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return {
                "path": path,
                "visited": visited_nodes,
            }

        for neighbor in grid.neighbors(*current):

            if neighbor not in visited:

                visited.add(neighbor)
                parent[neighbor] = current

                queue.append(neighbor)

    return None