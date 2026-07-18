def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'a')
    sdt = {'S': 1, 'D' : 2, 'T' : 3}
    for i in dartResult:
        if i in sdt:
            answer[-1] = answer[-1]**sdt[i]
        elif i == '#':
            answer[-1] *= -1
        elif i == '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif i == 'a':
            answer.append(10)
        else:
            answer.append(int(i))
    return sum(answer)