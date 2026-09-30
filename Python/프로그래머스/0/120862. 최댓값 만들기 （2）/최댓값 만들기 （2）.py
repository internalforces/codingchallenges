def solution(numbers):
    answer = []
    for i in numbers:
        if len(set(numbers)) == 1:
            return i*i
        for j in numbers:
            if i != j:
                a = i * j
                answer.append(a)
    return max(answer)