import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, h, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] > h:
                    visited[nx][ny] = True
                    q.append((nx, ny))

max_height = max(max(row) for row in grid)
answer = 0

for h in range(0, max_height + 1):
    visited = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] > h:
                bfs(i, j, h, visited)
                count += 1
    answer = max(answer, count)

print(answer)