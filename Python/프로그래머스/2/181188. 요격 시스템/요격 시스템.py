def solution(targets):
    targets.sort(key=lambda x: x[1])
    
    
    missile_count = 0
    last_missile_position = -float('inf')  
    
    for s, e in targets:
        
        if s >= last_missile_position:
            missile_count += 1
            last_missile_position = e  
    
    return missile_count
