n = int(input("Enter number of items: "))

weight = []
value = []

for i in range(n):
    weight.append(int(input("Enter weight: ")))
    value.append(int(input("Enter value: ")))

capacity = int(input("Enter knapsack capacity: "))

dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, capacity + 1):
        if weight[i - 1] <= j:
            dp[i][j] = max(
                value[i - 1] + dp[i - 1][j - weight[i - 1]],
                dp[i - 1][j]
            )
        else:
            dp[i][j] = dp[i - 1][j]

print("Maximum value:", dp[n][capacity])
