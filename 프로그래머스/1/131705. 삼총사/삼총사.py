from itertools import combinations
def solution(number):
    a = list(map(sum, combinations(number, 3))).count(0)
    return a