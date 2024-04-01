def print_comp_result(size, y, x):
    curr = video[y][x]

    for i in range(y, y + size):
        for j in range(x, x + size):
            if video[i][j] != curr:
                print('(', end='')
                print_comp_result(size // 2, y, x)
                print_comp_result(size // 2, y, x + size // 2)
                print_comp_result(size // 2, y + size // 2, x)
                print_comp_result(size // 2, y + size // 2, x + size // 2)
                print(')', end='')
                return

    print(curr, end='')


if __name__ == "__main__":
    N = int(input())
    video = [input() for _ in range(N)]

    print_comp_result(N, 0, 0)