import itertools

while True:
    array = list(map(int, input().split()))

    k = array[0]
    s_1 = array[1:]

    for i in itertools.combinations(s_1, 6):
        print(*i)

    if k == 0:
        exit()
    print()