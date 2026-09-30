def solution(num_list):
    answer = []
    odd_num, even_num = 0, 0
    for i in num_list:
        if i % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
    
    answer = [even_num, odd_num]
    return answer