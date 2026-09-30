def solution(n):
    # f(n) = 4f(n - 2) - f(n - 4)
    # f(0) = 1, f(2) = 3, f(4) = 11 f(6) = 41
    if n % 2 != 0:
        return 0 
    if n == 2:
        return 3
    if n == 4:
        return 11

    f1 = 3
    f2 = 11
    mod = 1000000007

    for i in range(6, n + 1, 2):
        f3 = (4 * f2 - f1) % mod
        f1, f2 = f2, f3

    return f2