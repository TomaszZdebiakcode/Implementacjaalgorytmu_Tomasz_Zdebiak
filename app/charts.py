import matplotlib.pyplot as plt


algorithms = ["A*", "BFS"]

visited_nodes = [343, 378]

times = [0.0010683, 0.0005866]


plt.figure(figsize=(8, 5))

plt.bar(algorithms, visited_nodes)

plt.title("Visited nodes comparison")

plt.ylabel("Visited nodes")

plt.show()