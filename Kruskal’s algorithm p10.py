
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for i in range(e):
    u, v, w = map(int, input("Enter edge and weight: ").split())
    edges.append([w, u, v])

edges.sort()

parent = list(range(n))
cost = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

print("Selected edges:")

for w, u, v in edges:
    a = find(u)
    b = find(v)

    if a != b:
        print(u, "-", v, ":", w)
        parent[a] = b
        cost += w

print("Minimum cost:", cost)
