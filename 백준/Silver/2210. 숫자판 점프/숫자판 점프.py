def dfs(x, y, number):
    if len(number) == 6:  
        if number not in result:  
            result.append(number)
        return

    dx = [1, -1, 0, 0]  
    dy = [0, 0, 1, -1]  
    for k in range(4):
        a = x + dx[k]
        b = y + dy[k]

        if 0 <= a< 5 and 0 <= b < 5:  # 범위 내에 있다면
            dfs(a, b, number + matrix[a][b])  # 6글자가 될 때 까지 재귀



matrix = [list(map(str, input().split())) for _ in range(5)]

result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])  
print(len(result))