def solution(hp):
    answer = 0
    while hp > 0:
        if hp >= 5:
            hp -= 5
            answer += 1
        if hp < 5 and hp >= 3:
            hp -= 3
            answer += 1
        elif hp < 3 and hp > 0:
            hp -= 1
            answer += 1
    return answer