#include <stdio.h>

int max(int a, int b) {
    return a > b ? a : b;
}

// n : 사냥터 수
// t : 방학 기간
// minExpToEnter : 입장에 필요한 최소 경험치
// expPerMinute : 1분마다 얻는 경험치
// travelTime : 사냥터 사이를 이동하는 데 걸리는 시간
int maplestory(int n, int t, int minExpToEnter[], int expPerMinute[], int travelTime[][200]){
    // dp[time] = time분일 때 얻을 수 있는 최대 경험치
    static int dp[1001];
    
    // 초기화
    for (int i = 0; i <= t; i++) {
        dp[i] = 0;
    }
    
    // 시작 가능한 사냥터 찾기 (minExp가 0인 사냥터)
    for (int start = 0; start < n; start++) {
        if (minExpToEnter[start] != 0) continue;
        
        // start 사냥터에서 시작하는 경우
        // 임시 dp 배열 사용
        static int temp[1001];
        for (int i = 0; i <= t; i++) {
            temp[i] = 0;
        }
        
        // 매 분마다 결정
        for (int time = 0; time < t; time++) {
            // 다음 시간의 경험치를 현재까지의 최대값으로 초기화
            temp[time + 1] = max(temp[time + 1], temp[time]);
            
            // 각 사냥터로 이동 시도
            for (int hunt = 0; hunt < n; hunt++) {
                // 현재 경험치로 입장 가능한지 확인
                if (temp[time] < minExpToEnter[hunt]) continue;
            }
        }
    }
    
    // dp[time][location] = time분에 location에 있을 때의 최대 경험치
    static int dpState[1001][200];
    
    // 초기화 (-1은 불가능한 상태)
    for (int i = 0; i <= t; i++) {
        for (int j = 0; j < n; j++) {
            dpState[i][j] = -1;
        }
    }
    
    // 경험치 0으로 입장 가능한 사냥터에서 시작
    for (int i = 0; i < n; i++) {
        if (minExpToEnter[i] == 0) {
            dpState[0][i] = 0;
        }
    }
    
    int maxTotalExp = 0;
    
    // 매 분마다 상태 전이
    for (int time = 0; time < t; time++) {
        for (int curr = 0; curr < n; curr++) {
            if (dpState[time][curr] == -1) continue;
            
            int currExp = dpState[time][curr];
            
            // 현재 사냥터에서 계속 사냥
            int newExp = currExp + expPerMinute[curr];
            dpState[time + 1][curr] = max(dpState[time + 1][curr], newExp);
            maxTotalExp = max(maxTotalExp, newExp);
            
            // 다른 사냥터로 이동
            for (int next = 0; next < n; next++) {
                if (next == curr) continue;
                
                int moveTime = travelTime[curr][next];
                int arrivalTime = time + moveTime;
                
                // 이동 후 도착 시간이 방학 기간을 넘지 않고,
                // 현재 경험치로 입장 가능한 경우
                if (arrivalTime <= t && currExp >= minExpToEnter[next]) {
                    dpState[arrivalTime][next] = max(dpState[arrivalTime][next], currExp);
                    maxTotalExp = max(maxTotalExp, currExp);
                }
            }
        }
    }
    
    printf("%d\n", maxTotalExp);
    return maxTotalExp;
}

int main(){
    int n, t;
    static int minExpToEnter[200];
    static int expPerMinute[200];
    static int travelTime[200][200];

    scanf("%d %d", &n, &t);

    for (int i = 0; i < n; i++){
        scanf("%d %d", &minExpToEnter[i], &expPerMinute[i]);
    }
    
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            scanf("%d", &travelTime[i][j]);
        }
    }

    maplestory(n, t, minExpToEnter, expPerMinute, travelTime);
    
    return 0;
}