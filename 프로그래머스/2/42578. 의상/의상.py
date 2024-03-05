def solution(clothes):
    answer = {}
    
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1
    print(answer)  
    result = 1
    
    for i in answer.values():
        result *= (i+1)
        print(result)
    return result - 1