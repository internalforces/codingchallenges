def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer += i
    cost = 0
    cost = price * answer
    if (cost > money):
        return (cost - money)
    else:
        return 0
    #return answer