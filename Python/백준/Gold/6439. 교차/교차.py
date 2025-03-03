import sys

def ccw(ax, ay, bx, by, cx, cy):
    
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    
    ccw1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    ccw2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    
    # 두 선분이 한 직선 위에 있을 때
    if ccw1 == 0 and ccw2 == 0:
        return (min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and
                min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2))
    
    return ccw1 <= 0 and ccw2 <= 0

# 첫 번째 줄: 테스트 케이스 개수
T = int(sys.stdin.readline().strip())

# 각 테스트 케이스에 대해 처리
for _ in range(T):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().strip().split())

    # 직사각형의 좌표 정렬
    x_left, x_right = min(x3, x4), max(x3, x4)
    y_top, y_bottom = max(y3, y4), min(y3, y4)

    # 1. 선분의 한쪽 끝점이 직사각형 내부에 있는 경우
    if (x_left <= x1 <= x_right and y_bottom <= y1 <= y_top) or \
       (x_left <= x2 <= x_right and y_bottom <= y2 <= y_top):
        print("T")
        continue

    # 2. 선분이 직사각형의 변과 교차하는 경우 (사각형의 네 변과 교차 판별)
    intersects = (
        is_intersect(x1, y1, x2, y2, x_left, y_top, x_left, y_bottom) or  # 왼쪽 변
        is_intersect(x1, y1, x2, y2, x_right, y_top, x_right, y_bottom) or  # 오른쪽 변
        is_intersect(x1, y1, x2, y2, x_left, y_bottom, x_right, y_bottom) or  # 아래쪽 변
        is_intersect(x1, y1, x2, y2, x_left, y_top, x_right, y_top)  # 위쪽 변
    )

    print("T" if intersects else "F")