def solution(s):
    answer = []
    
    for qo in s:
        if qo == "(":
            answer.append(qo)
        else:
            if answer:
                answer.pop()
            else:
                return False
        
    if answer:
        print(answer)
        return False
    return True