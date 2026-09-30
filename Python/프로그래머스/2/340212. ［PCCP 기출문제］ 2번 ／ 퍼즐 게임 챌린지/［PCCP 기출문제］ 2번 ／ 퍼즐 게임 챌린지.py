def solution(diffs, times, limit):
    def complete(level):
        total_time = 0
        prev_time = 0  
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            
            if diff <= level:
                total_time += time_cur  
            else:
                mistakes = diff - level  
                total_time += mistakes * (time_cur + prev_time) + time_cur  
            prev_time = time_cur  
            
            if total_time > limit:  
                return False
        return total_time <= limit
    
    left, right = 1, max(diffs)
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if complete(mid):  
            answer = mid
            right = mid - 1
        else:  
            left = mid + 1
    
    return answer
