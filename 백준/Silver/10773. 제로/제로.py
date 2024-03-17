n = int(input())
a = []
for i in range(n):
    k = int(input())
    a.append(k)

stack = []
for i in a:
    if i == 0:
        stack.pop() if stack else None
    else:
        stack.append(i)
print(sum(stack))