def dfs(grid, visited, i, j, H, W):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                stack.append((nx, ny))

T = int(input())

for _ in range(T):
    H, W = map(int, input().split())

    grid = []

    for _ in range(H):
        row = input()
        grid.append(row)

    visited = [[False] * W for _ in range(H)]

    count = 0

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                count += 1

                visited[i][j] = True
                dfs(grid, visited, i, j, H, W)


    print(count)
