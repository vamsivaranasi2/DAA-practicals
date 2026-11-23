
graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    node = input("Enter vertex: ")
    graph[node] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = input("Enter edge: ").split()
    graph[u].append(v)
    graph[v].append(u)

def dfs(node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for i in graph[node]:
            dfs(i, visited)

def bfs(start):
    visited = [start]
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

start = input("Enter starting vertex: ")

print("DFS Traversal:")
dfs(start, [])

print("\nBFS Traversal:")
bfs(start)
