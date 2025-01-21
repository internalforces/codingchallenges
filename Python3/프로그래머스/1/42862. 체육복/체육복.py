def solution(n, lost, reserve):
    answer = 0
    reserve_1 = set(reserve) - set(lost)
    lost_1 = set(lost) - set(reserve)
    
    for i in reserve_1:
        if i-1 in lost_1:
            lost_1.remove(i-1)
            print(lost_1)
        elif i+1 in lost_1:
            lost_1.remove(i+1)
            print(lost_1)

    
    return n - len(lost_1)