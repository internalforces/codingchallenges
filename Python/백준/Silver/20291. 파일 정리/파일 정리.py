import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
file_name = []
for i in range(n):
    file = input().strip()
    file_a = file.split('.')[-1]
    file_name.append(file_a)
file_name.sort()
count = Counter(file_name)

for file_a, count in count.items():
    print(file_a, count)