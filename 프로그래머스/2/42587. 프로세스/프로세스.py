from collections import deque
def solution(priorities, location):
    answer = 1
    d1 = deque(priorities)
    d2 = deque(range(len(priorities)))
    maximum = max(d1)
    
    while d1:
        x = d1.popleft()
        y = d2.popleft()
        if x == maximum and y == location :
            return answer
        elif x == maximum :
            answer += 1
            maximum = max(d1)
        else :
            d1.append(x)
            d2.append(y)
            
    return answer