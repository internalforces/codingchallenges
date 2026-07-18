def solution(survey, choices):
    answer = ''
    dicts = {'T' : 0, 'R' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    for i in range(len(survey)):
        if choices[i] > 4:
            dicts[survey[i][0]] += choices[i] - 4
        
        elif choices[i] < 4:
            dicts[survey[i][1]] += 4 - choices[i]
            
        #print(dicts)
    if dicts['T'] >= dicts['R']:
        answer += 'R'
    else:
        answer += 'T'
    if dicts['F'] >= dicts['C']:
        answer += 'C'
    else:
        answer += 'F'
    if dicts['M'] >= dicts['J']:
        answer += 'J'
    else:
        answer += 'M'
    if dicts['N'] >= dicts['A']:
        answer += 'A'
    else:
        answer += 'N'
    return answer