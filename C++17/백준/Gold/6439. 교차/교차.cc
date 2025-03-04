#include <iostream>
using namespace std;

// CCW (Counter Clockwise) 판별 함수
int ccw(int ax, int ay, int bx, int by, int cx, int cy) {
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
}

// 두 선분이 교차하는지 확인하는 함수
bool is_intersect(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
    int ccw1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4);
    int ccw2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2);
    
    // 두 선분이 한 직선 위에 있을 때
    if (ccw1 == 0 && ccw2 == 0) {
        return (min(x1, x2) <= max(x3, x4) && min(x3, x4) <= max(x1, x2) &&
                min(y1, y2) <= max(y3, y4) && min(y3, y4) <= max(y1, y2));
    }
    
    return ccw1 <= 0 && ccw2 <= 0;
}

int main() {
    int T;
    cin >> T;
    
    while (T--) {
        int x1, y1, x2, y2, x3, y3, x4, y4;
        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;
        
        // 직사각형의 좌표 정렬
        int x_left = min(x3, x4), x_right = max(x3, x4);
        int y_top = max(y3, y4), y_bottom = min(y3, y4);
        
        // 1. 선분의 한쪽 끝점이 직사각형 내부에 있는 경우
        if ((x_left <= x1 && x1 <= x_right && y_bottom <= y1 && y1 <= y_top) ||
            (x_left <= x2 && x2 <= x_right && y_bottom <= y2 && y2 <= y_top)) {
            cout << "T" << endl;
            continue;
        }
        
        // 2. 선분이 직사각형의 변과 교차하는 경우
        bool intersects = (
            is_intersect(x1, y1, x2, y2, x_left, y_top, x_left, y_bottom) ||  // 왼쪽 변
            is_intersect(x1, y1, x2, y2, x_right, y_top, x_right, y_bottom) ||  // 오른쪽 변
            is_intersect(x1, y1, x2, y2, x_left, y_bottom, x_right, y_bottom) ||  // 아래쪽 변
            is_intersect(x1, y1, x2, y2, x_left, y_top, x_right, y_top)  // 위쪽 변
        );
        
        cout << (intersects ? "T" : "F") << endl;
    }
    
    return 0;
}