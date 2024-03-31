def solution(bridge_length, weight, truck_weights):
    time = 0
    passing_bridge = [0] * bridge_length
    sum_truck = 0
    
    while truck_weights:    
        passing_bridge.pop(0)
        if truck_weights:
            sum_truck += truck_weights[0]
            
            if sum_truck <= weight:
                passing_bridge.append(truck_weights.pop(0))
            else:
                sum_truck -= truck_weights[0]
                passing_bridge.append(0) # 지나는 시간 무게 0 초과 예시) 1~2, 6~7
            
            sum_truck -= passing_bridge[0]
            time += 1
            
    return time + len(passing_bridge)