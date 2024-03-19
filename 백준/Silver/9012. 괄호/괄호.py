n = int(input())
a = []
for i in range(n):
    k = input()
    a.append(k)

for s in a:
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
