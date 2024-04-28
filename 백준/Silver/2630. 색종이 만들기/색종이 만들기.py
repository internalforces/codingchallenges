def cut_paper(init_y, init_x, length):
    init_color = colored_paper[init_y][init_x]
    is_identical = True
    for i in range(init_y, init_y + length):
        for j in range(init_x, init_x + length):
            if init_color != colored_paper[i][j]:
                is_identical = False
                break

    if is_identical:
        color_counter[init_color] += 1
    else:
        cut_paper(init_y, init_x, length // 2)
        cut_paper(init_y + length // 2, init_x, length // 2)
        cut_paper(init_y, init_x + length // 2, length // 2)
        cut_paper(init_y + length // 2, init_x + length // 2, length // 2)


N = int(input())
colored_paper = []
for _ in range(N):
    row = list(map(int, input().split()))
    colored_paper.append(row)

color_counter = [0, 0]  # white count, blue count
cut_paper(0, 0, N)

print(color_counter[0])
print(color_counter[1])