def coin_change_ways(T, test_cases):
    results = []
    
    for case in test_cases:
        N, coins, M = case
        dp = [0] * (M + 1)
        dp[0] = 1
        
        for coin in coins:
            for amount in range(coin, M + 1):
                dp[amount] += dp[amount - coin]
        
        results.append(dp[M])
    
    return results

T = int(input().strip())
test_cases = []

for _ in range(T):
    N = int(input().strip())
    coins = list(map(int, input().strip().split()))
    M = int(input().strip())
    test_cases.append((N, coins, M))

results = coin_change_ways(T, test_cases)
for result in results:
    print(result)