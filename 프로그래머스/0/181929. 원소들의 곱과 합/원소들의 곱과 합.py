def solution(num_list):
    sum_num = sum(num_list)
    ans = 1
    for i in num_list:
        ans *= i
    if ans < sum_num*sum_num:
        return 1
    else:
        return 0