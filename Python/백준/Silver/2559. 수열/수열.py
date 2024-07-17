import sys
input = sys.stdin.readline

result = []
N, M = map(int, input().split())
temp = list(map(int, input().split()))

current_sum = sum(temp[:M])
max_sum = current_sum

for i in range(1, N - M + 1):
    current_sum = current_sum - temp[i - 1] + temp[i + M - 1]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)