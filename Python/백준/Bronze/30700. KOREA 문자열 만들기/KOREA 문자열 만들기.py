import sys

input = sys.stdin.readline

s = input().strip()

korea = ["K", "O", "R", "E", "A"]
count = 0
index = 0

for char in s:
    if char == korea[index]:
        count += 1
        index += 1
        if index == 5:
            index = 0

print(count)