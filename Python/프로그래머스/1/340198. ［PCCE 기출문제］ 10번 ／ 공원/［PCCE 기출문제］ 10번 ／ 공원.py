def solution(mats, park):
    n = len(park)
    m = len(park[0]) if n > 0 else 0

    dp = [[0] * m for _ in range(n)]  
    answer = 0

    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":  
                if i == 0 or j == 0:  
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                if dp[i][j] in mats and dp[i][j] > answer:
                    answer = dp[i][j]
            if answer == 0:
                answer = -1
    return answer