n = int(input())
a = []
for i in range(n):
    k = int(input())
    a.append(k)

answer = []
for i in a:
    if i == 0:
        del answer[-1]
    else:
        answer.append(i)
print(sum(answer))