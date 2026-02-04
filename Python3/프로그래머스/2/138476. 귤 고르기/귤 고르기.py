from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    cnt = Counter(tangerine)
    choice = sorted(cnt.values(), reverse = True)
    
    s = 0
    for c in choice:
        s += c
        answer += 1
        
        if s >= k:
            break
            
    return answer