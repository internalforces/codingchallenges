from string import ascii_lowercase
def solution(s, skip, index):
    answer = ''
    skip = list(skip)
    alpha = list(ascii_lowercase)
    
    for i in skip:
        alpha.remove(i)
    alpha = alpha*3
    print(alpha)
    for j in s:
        answer += alpha[alpha.index(j) + index]
    return answer