def solution(today, terms, privacies):
    answer = []
    
    time_dict = dict()
    year, month, day = int(today[0:4]), int(today[5:7]), int(today[8:])
    
    today_a = (year-2000)*12*28 + (month-1)*28 + day
    
    
    for term in terms : 
        case = term[0]
        time_dict[case] = int(term[2:])
    
    
    for i in range(len(privacies)):
        date, case = privacies[i].split()
        p_year, p_month, p_day = int(privacies[i][0:4]), int(privacies[i][5:7]), int(privacies[i][8:10])
        
        today_p = (p_year-2000)*12*28 + (p_month-1)*28 + p_day

        
        today_p += time_dict[case]*28
        
        if today_p <= today_a:
            answer.append(i+1)
            
    return answer