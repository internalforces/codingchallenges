n = int(input())
a = []
for i in range(n):
    k = int(input())
    a.append(k)

stack = []
index = 0
result = []
for i in range(1, n + 1): 
    stack.append(i)
    result.append('+')
    
    while stack and stack[-1] == a[index]:
        stack.pop()  
        index += 1  
        result.append('-')

if not stack:
    for r in result:
        print(r)
else:
    print("NO")
