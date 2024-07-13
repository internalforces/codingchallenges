import sys
input = sys.stdin.readline
from itertools import permutations
k = int(input())
E = list(map(str, input().split()))
ans = []
num = [i for i in range(10)]
for per in permutations(num, k+1):
    for i in range(len(E)):
        if E[i] == '<':
            if per[i] > per[i+1]: break
        else:
            if per[i] < per[i+1]: break
    else:
        ans.append(per)
ans.sort()
print(''.join(map(str,ans[-1])))
print(''.join(map(str,ans[0])))