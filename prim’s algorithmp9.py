
n = int(input("Enter number of vertices: "))

graph = []

print("Enter the adjacency matrix:")
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [0] * n
visited[0] = 1

edges = 0
cost = 0

while edges < n - 1:
    minimum = 999
    a = -1
    b = -1

    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        a = i
                        b = j

    if a == -1:
        print("Graph is not connected")
        break

    print(a, "-", b, ":", minimum)
    cost += minimum
    visited[b] = 1
    edges += 1

if edges == n - 1:
    print("Minimum cost:", cost)
