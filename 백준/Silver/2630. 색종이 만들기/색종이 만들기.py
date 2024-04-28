def cut_paper(x, y, length):
    color = colored_paper[x][y]
    is_identical = True
    for i in range(x, x + length):
        for j in range(y, y + length):
            if color != colored_paper[i][j]:
                is_identical = False
                break

    if is_identical:
        color_counter[color] += 1
    else:
        cut_paper(x, y, length // 2)
        cut_paper(x + length // 2, y, length // 2)
        cut_paper(x, y + length // 2, length // 2)
        cut_paper(x + length // 2, y + length // 2, length // 2)


N = int(input())
colored_paper = []
for _ in range(N):
    row = list(map(int, input().split()))
    colored_paper.append(row)

color_counter = [0, 0]  # white count, blue count
cut_paper(0, 0, N)

print(color_counter[0])
print(color_counter[1])