
n = int(input("Enter number of cities: "))

cost = []

print("Enter cost matrix:")
for i in range(n):
    cost.append(list(map(int, input().split())))

visited = [False] * n
visited[0] = True

total = 0
current = 0

print("Path:", current, end=" ")

for i in range(n - 1):
    minimum = 999
    next_city = -1

    for j in range(n):
        if not visited[j] and cost[current][j] < minimum:
            minimum = cost[current][j]
            next_city = j

    if next_city == -1:
        print("\nNo complete tour possible")
        break

    visited[next_city] = True
    total += minimum
    current = next_city
    print(current, end=" ")

if all(visited):
    total += cost[current][0]
    print("0")
    print("Total cost:", total)
