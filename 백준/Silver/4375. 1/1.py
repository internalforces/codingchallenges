while 1:
    try:
        n = int(input())
        k = 1
        num = 1
        while 1:
            if (num % n == 0):
                print(k)
                break
            else:
                num = num * 10 + 1
                k += 1
    except:
        break
                