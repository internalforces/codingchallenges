def solution(n):
    MOD = 1000000007
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    prev1, prev2 = 1, 2  # f(1), f(2)
    
    for i in range(3, n + 1):
        curr = (prev1 + prev2) % MOD
        prev1, prev2 = prev2, curr
    
    return prev2