def solution(my_string):
    k = 0
    p = ''
    for i in my_string :

        if i in p :
            continue 
        else :
            p += i

    answer = p
    return answer