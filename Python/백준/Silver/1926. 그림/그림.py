import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    size = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    size += 1
    return size

count = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            size = bfs(i, j)
            count += 1
            max_size = max(size, max_size)

print(count)
print(max_size)