def solution(numbers, hand):
    answer = ''
    pad = {
        1:(3,0), 2:(3,1), 3:(3,2),
        4:(2,0), 5:(2,1), 6:(2,2),
        7:(1,0), 8:(1,1), 9:(1,2),
        "*":(0,0), 0:(0,1), "#":(0,2)
    }
    l_son = pad["*"]
    r_son = pad["#"]
    
    for num in numbers:
        num_pad = pad[num]
        
        if num in [1,4,7]:
            answer += "L"
            l_son = num_pad
            
        elif num in [3,6,9]:
            answer += "R"
            r_son = num_pad
            
        elif num in [2,5,8,0]:
            l_dis = abs(num_pad[0]-l_son[0]) + abs(num_pad[1]-l_son[1])
            r_dis = abs(num_pad[0]-r_son[0]) + abs(num_pad[1]-r_son[1])
            if l_dis < r_dis:
                answer += "L"
                l_son = num_pad
                
            elif l_dis > r_dis:
                answer += "R"
                r_son = num_pad
                
            else:
                if hand == "left":
                    answer += "L"
                    l_son = num_pad
                else:
                    answer += "R"
                    r_son = num_pad
    return answer