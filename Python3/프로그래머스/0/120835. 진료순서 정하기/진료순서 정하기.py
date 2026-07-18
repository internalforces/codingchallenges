import copy

def solution(emergency):
    answer = []
    
    price = copy.deepcopy(emergency)
    price.sort(reverse=True)
    
    #print(emergency)
    #print(price)
    
    for i in range(len(emergency)):
        answer.append(price.index(emergency[i])+1)
    
    return answer