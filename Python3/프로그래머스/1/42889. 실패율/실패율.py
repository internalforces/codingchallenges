def solution(N, stages):
    answer = []
    length = len(stages)
    # 1부터 N까지 스테이지를 하나씩 살펴보며
    for i in range(1, N+1):
        # 아직 클리어하지 못한 플레이어의 수 세기
        count = stages.count(i)
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        # 다음 스테이지에 도달한 플레이어의 수 계산
        length -= count
        # 배열에 (스테이지 번호, 실패율) 추가
        answer.append((i, fail))
    # 실패율 내림차순을 기준으로 정렬
    answer = sorted(answer, key=lambda x: x[1], reverse = True)
    # 각 스테이지 번호를 실패율의 내림차순으로 정렬
    answer = [i[0] for i in answer]
    return answer