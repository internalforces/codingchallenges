from math import ceil

def solution(progresses, speeds):
    answer = []
    
    max_time = 0
    cnt = 1
    
    for i in range(len(progresses)):
        time = ceil((100 - progresses[i])/speeds[i])
          
        if max_time < time:
            max_time = time
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
            
    return answer[1:]+[cnt]