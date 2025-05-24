import sys

input = sys.stdin.readline

n = int(input())
n = bin(n)[2:]
n = n[::-1]
n = int(n, 2)
print(n)