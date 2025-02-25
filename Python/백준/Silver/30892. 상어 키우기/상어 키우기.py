import sys

# 입력 받기
n, k, t = map(int, sys.stdin.readline().split())
sharks = list(map(int, sys.stdin.readline().split()))
sharks.sort()  

stack = []
idx = 0
eaten = 0

while eaten < k:
    while idx < n and sharks[idx] < t:
        stack.append(sharks[idx])
        idx += 1

    if not stack:
        break

    best = stack.pop()
    t += best
    eaten += 1

print(t)
