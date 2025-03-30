import sys

input = sys.stdin.readline

stack = []

s = input().strip()
boom = input().strip()

for char in s:
    stack.append(char)

    if stack[-len(boom):] == list(boom):
        for _ in range(len(boom)):
            stack.pop()

if stack:
    result = ''.join(stack)
    print(result)
else:
    print("FRULA")