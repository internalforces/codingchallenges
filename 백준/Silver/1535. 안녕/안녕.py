def max_joy(N, L, J):
    max_health = 100
    dp = [0] * max_health

    for i in range(N):
        for health in range(max_health - 1, L[i] - 1, -1):
            dp[health] = max(dp[health], dp[health - L[i]] + J[i])

    return max(dp)

N = int(input().strip())
L = list(map(int, input().strip().split()))
J = list(map(int, input().strip().split()))

print(max_joy(N, L, J))
