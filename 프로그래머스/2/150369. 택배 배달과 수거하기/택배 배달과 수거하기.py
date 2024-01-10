def solution(cap, n, deliveries, pickups):
    answer = 0  # 최소 이동 거리를 저장할 변수

    give = 0  # 배달해야 할 상자 수
    get = 0   # 수거해야 할 상자 수
    
    # 각 집에 대해 거꾸로 반복문을 돕니다.
    for i in range(n-1, -1, -1):
        # 해당 집에 배달하거나 수거해야 할 상자가 있다면
        if deliveries[i] != 0 or pickups[i] != 0:
            cnt = 0  # 이동 횟수를 저장할 변수
            # 배달하거나 수거해야 할 상자 수가 충족될 때까지 반복
            while give < deliveries[i] or get < pickups[i]:
                cnt += 1  # 이동 횟수 증가
                give += cap  # 트럭의 적재용량만큼 배달 상자 증가
                get += cap   # 트럭의 적재용량만큼 수거 상자 증가
            
            # 배달하고 수거한 상자 수만큼 빼기
            give -= deliveries[i]
            get -= pickups[i]
            
            # 이동 거리 계산하여 더하기
            # (i + 1)는 물류창고에서 해당 집까지의 거리, cnt는 이동 횟수, 2는 왕복
            answer += (i + 1) * cnt * 2

    return answer  # 최소 이동 거리 반환