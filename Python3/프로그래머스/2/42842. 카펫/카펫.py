def solution(brown, yellow):
    # 노란색 타일 가로 : m
    # 노란색 타일 세로 : n
    # 노란색 타일 개수 : m*n = yellow
    # 갈색 타일의 개수 : 2(m+n+2) = brown
    m=(brown/2-2+(((brown/2)-2)**2-4*yellow)**0.5)/2
    n=yellow/m
    return [m+2, n+2]