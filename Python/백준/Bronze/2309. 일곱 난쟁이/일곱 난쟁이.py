import sys

input = sys.stdin.readline

a = [int(input()) for _ in range(9)]
total = sum(a)

found = False
for i in range(9):
    for j in range(i + 1, 9):
        if total - a[i] - a[j] == 100:
            result = [a[k] for k in range(9) if k != i and k != j]
            result.sort()
            for num in result:
                print(num)
            found = True
            break
    if found:
        break

