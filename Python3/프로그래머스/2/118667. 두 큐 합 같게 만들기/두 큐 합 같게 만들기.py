from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total_sum = sum1 + sum2
    
    if total_sum % 2 != 0:
        return -1
    
    target_sum = total_sum // 2
    count = 0
    
    max_operations = len(queue1) + len(queue2) * 2
    
    while count <= max_operations:
        if sum1 == target_sum:
            return count
        elif sum1 < target_sum:
            value = queue2.popleft()
            queue1.append(value)
            sum1 += value
            sum2 -= value
        else:
            value = queue1.popleft()
            queue2.append(value)
            sum1 -= value
            sum2 += value
        
        count += 1
    
    return -1
