import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

seat = [list(input().rstrip()) for _ in range(N)]
result = 0

for i in range(N):
    cheak = 1
    for j in range(M):
        if seat[i][j] == '0':
            if cheak >= K:
                result += 1
            cheak += 1
        else:
            cheak = 1
print(result)