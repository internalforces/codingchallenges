def solution(n):
    lst0 = []
    start_num = 2
    while 1:
        if n == 1:
            return lst0
        elif n % start_num == 0:
            n = n / start_num
            if start_num not in lst0:
                lst0.append(start_num)
        elif n % start_num != 0:
            start_num += 1