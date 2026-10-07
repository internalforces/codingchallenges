from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil = [0] * m
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True
        size = 0
        columns = set()

        while queue:
            x, y = queue.popleft()
            size += 1
            columns.add(y)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if land[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

        return size, columns

    for r in range(n):
        for c in range(m):
            if land[r][c] == 1 and not visited[r][c]:
                size, columns = bfs(r, c)

                for col in columns:
                    oil[col] += size

    return max(oil)