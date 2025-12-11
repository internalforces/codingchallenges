#include <iostream>
#include <algorithm>

using namespace std;

int min_distance(int x, int y, int w, int h){
    int dist_left = x;
    int dist_right = w - x;
    int dist_bottom = y;
    int dist_top = h - y;

    int result = min({dist_left, dist_right, dist_bottom, dist_top});
    return result;
}

int main(){
    int x, y, w, h;
    cin >> x >> y >> w >> h;

    cout << min_distance(x, y, w, h) << "\n";
    return 0;
}