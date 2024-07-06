def mario_100(scores):
    mario_score = 0
    mario_sum = 0

    for score in scores:
        mario_sum += score

        if mario_sum == 100:
            return 100
        elif mario_sum > 100:
            if abs(100 - mario_sum) < abs(100 - mario_score):
                return mario_sum
            elif abs(100 - mario_sum) == abs(100 - mario_score):
                return max(mario_sum, mario_score)
            else:
                return mario_score
        mario_score = mario_sum
        # mario_sum이 100을 넘지않으면  mario_score 갱신

    return mario_score

scores = []
for _ in range(10):
    score = int(input())
    scores.append(score)

result = mario_100(scores)
print(result)