import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

result = 0
for i in range(len(a)):
    b_max = max(b)
    result += a[i] * b_max
    b.remove(b_max)

print(result)