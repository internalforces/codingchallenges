def solution(n):
    answer = ''
    list_n = list(map(int, str(n)))
    print(list_n)
    list_n.sort(reverse = True)
    for i in list_n:
        answer += str(i)
    return int(answer)