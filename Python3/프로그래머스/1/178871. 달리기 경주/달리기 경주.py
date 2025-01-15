def solution(players, callings):
    # 요소와 인덱스를 매핑한 사전 생성
    index_map = {player: i for i, player in enumerate(players)}
    
    for call in callings:
        idx = index_map[call]
        if idx > 0:  # 이미 첫 번째가 아니라면
            # 현재와 앞의 요소 교환
            players[idx], players[idx - 1] = players[idx - 1], players[idx]
            
            # 사전에서 인덱스 갱신
            index_map[players[idx]] = idx
            index_map[players[idx - 1]] = idx - 1
            
    return players