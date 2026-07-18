def solution(x):
    return not bool(x%sum(list(map(int, list(str(x))))))