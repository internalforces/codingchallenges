N = int(input())
inversion = list(map(int, input().split()))
origin = []

for j in range(N):
    if inversion[j] == 0:
        origin.append(j + 1)
    else:
        pos = len(origin) - inversion[j]
        origin.insert(pos, j + 1)

print(*origin)
