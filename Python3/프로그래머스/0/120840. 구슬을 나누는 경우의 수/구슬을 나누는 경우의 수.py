def solution(balls, share):
    k = 1
    # n combination m
    for n, m in zip(range(balls-share+1, balls+1), range(1, share+1)):
        k = k*n/m

    answer = k
    return answer