nanj = [0] * 9
for i in range(0, 9):
    nanj[i] = int(input())

an_nanj = sum(nanj) - 100

j = 0
while j < len(nanj):
    k = j + 1  
    while k < len(nanj):
        if nanj[j] + nanj[k] == an_nanj:
            del nanj[k]  
            del nanj[j]
            j -= 1  
            break
        k += 1
    j += 1

for i in nanj:
    print(i)  