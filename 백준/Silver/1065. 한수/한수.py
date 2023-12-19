n = int(input())

count = 0
check = 100 

if n < 100:
    print(n)
else:
    while check <= n:
        if check // 100 - (check % 100) // 10 == (check % 100) // 10 - check % 10:
            count += 1
        check += 1
    print(99 + count)