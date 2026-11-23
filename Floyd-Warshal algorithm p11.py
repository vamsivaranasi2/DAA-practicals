
n = int(input("Enter number of vertices: "))

graph = []

print("Enter the cost matrix (use 999 for no edge):")
for i in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

print("Shortest distance matrix:")
for row in graph:
    print(*row)
