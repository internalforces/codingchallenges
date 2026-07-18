from collections import Counter
def solution(topping):
    answer = 0
    dic = Counter(topping)
    s = set()
    for i in topping:
        dic[i] -= 1
        s.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(s):
            answer += 1
    return answer