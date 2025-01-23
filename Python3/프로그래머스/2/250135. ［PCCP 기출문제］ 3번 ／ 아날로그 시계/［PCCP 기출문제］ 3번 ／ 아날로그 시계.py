def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    hcount = 0
    mcount = 0
    
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    
    if start == 0 or start == 60*60*12 :
        answer += 1

    for i in range(start, end) :
        s = (i * 6) % 360
        m = (i / 10) % 360
        h = (i / 120) % 360

        if (i + 1) * 6 % 360 == 0:
            ns = 360
        else:
            ns = (i + 1) * 6 % 360
        
        if (i + 1) / 10 % 360 == 0:
            nm = 360
        else:
            nm = (i + 1) / 10 % 360
        
        if (i + 1) / 120 % 360 == 0:
            nh = 360
        else:
            nh = (i + 1) / 120 % 360
            
            
        if s < h and ns >= nh :
            hcount += 1
            
        if s < m and ns >= nm :
            mcount += 1
            
        if ns == nm == nh :
            answer -= 1
            
    answer += hcount + mcount
    print(answer)
    return answer