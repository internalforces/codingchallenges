def solution(n):
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