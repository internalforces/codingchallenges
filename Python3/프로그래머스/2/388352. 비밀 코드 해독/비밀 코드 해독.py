from itertools import combinations

def solution(n, q, ans):
    answer = 0
    num = []
    m = len(ans)
    
    for i in range(1, n+1):
        num.append(i)
    
    for combi in combinations(num, 5):
        ok = True
        for i in range(m):
            cnt = 0
            for j in q[i]:
                if j in combi:
                    cnt += 1
            if cnt != ans[i]:
                ok = False
                break
        if ok:
            answer +=1
            
        
    return answer