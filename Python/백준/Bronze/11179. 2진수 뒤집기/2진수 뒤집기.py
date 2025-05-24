import sys

input = sys.stdin.readline

n = int(input())
a = bin(n)[2:]
a = a[::-1]
a = int(a, 2)
print(a)