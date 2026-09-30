import collections

def solution(participant, completion):
    p = collections.Counter(participant)
    c = collections.Counter(completion)
    
    answer = p - c
    print(answer)
    
    return list(answer.keys())[0]
    