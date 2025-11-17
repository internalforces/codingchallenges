import sys

input = sys.stdin.readline

test = int(input())

for i in range(test):
    n = int(input())
    clothes = {}

    for j in range(n):
        name, kind = input().split()
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1

    result = 1
    for count in clothes.values():
        result *= (count + 1)

    result -= 1

    print(result)
