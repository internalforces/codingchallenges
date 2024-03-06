N = int(input())
insin = list(map(int, input().split()))
arr = []

for i in range(N):
    if insin[i] == 0:
        arr.append(i + 1)
    else:
        cg = len(arr) - insin[i]
        arr.insert(cg, i + 1)

print(*arr)
