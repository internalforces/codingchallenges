def solution(video_len, pos, op_start, op_end, commands):
    vl = (int(video_len[0])*10 + int(video_len[1]))*60 + int(video_len[3])*10 + int(video_len[4])
    ps = (int(pos[0])*10 + int(pos[1]))*60 + int(pos[3])*10 + int(pos[4])
    os = (int(op_start[0])*10 + int(op_start[1]))*60 + int(op_start[3])*10 + int(op_start[4])
    oe = (int(op_end[0])*10 + int(op_end[1]))*60 + int(op_end[3])*10 + int(op_end[4])
    
    if ps >= os and ps <= oe:
        ps = oe

    for i in commands:
        if i == "prev":
            ps -= 10  
            if ps < 0:  
                ps = 0
        elif i == "next":
            ps += 10  
            
        if ps > vl:
            ps = vl
        
        if ps >= os and ps <= oe:
            ps = oe

    minutes = ps // 60
    seconds = ps % 60
    answer = f"{minutes:02}:{seconds:02}"
    
    return answer
