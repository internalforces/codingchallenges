from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

ans = 0
answer = []
arrs = permutations(arr, n)
for arr in arrs:
    for i in range(len(arr)-1):
       ans += abs(arr[i]-arr[i+1])

    answer.append(ans)

    ans = 0

print(max(answer))