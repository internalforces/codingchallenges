def solution(n):
    answer = n ** 0.5
    
    if int(answer) == answer:
        return 1
    return 2