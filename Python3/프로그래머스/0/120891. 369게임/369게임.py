def solution(order):
    order = str(order)
    order_l = list(order)
    answer = 0
    print(order_l)
    for i in range(len(order_l)):
        if order_l[i] == '3' or order_l[i] == '6' or order_l[i] == '9':
            answer += 1
    return answer