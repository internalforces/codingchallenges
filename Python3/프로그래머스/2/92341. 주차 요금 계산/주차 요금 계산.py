import math
 
def solution(fees, records):
    car_info = {}
    fee_list = []
    max_time = 23 * 60 + 59
    for record in records:
        t, c, _ = record.split(" ")
        t = int(t[:2]) * 60 + int(t[3:])
        
        if c not in car_info:
            car_info[c] = [0, 0]
        
        car_info[c][0] += ((max_time - t) * (-1) ** (car_info[c][1]))
        car_info[c][1] += 1
    
    for _, t in sorted(car_info.items(), key = lambda x : x[0]):
        
        extra_t = t[0] - fees[0] if t[0] > fees[0] else 0
        
        fee = fees[1] + math.ceil((extra_t) / fees[2]) * (fees[3])
        fee_list.append(fee)
    return fee_list