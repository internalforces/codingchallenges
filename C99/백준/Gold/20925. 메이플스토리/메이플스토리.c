#include <stdio.h>

#define MAXN 200
#define MAXT 1000
#define NEG -1LL

long long max(long long a, long long b) {
    return a > b ? a : b;
}

// n : 사냥터 수
// T : 방학 기간(분)
// c : 입장에 필요한 최소 경험치
// e : 1분마다 얻는 경험치
// travelTime[i][j] : i -> j 이동 및 입장까지 걸리는 시간
long long maplestory(int n, int T, int c[], int e[], int travelTime[][MAXN]) {
    static long long dp[MAXT + 1][MAXN];

    // dp 초기화 (도달 불가능은 -1로)
    for (int t = 0; t <= T; t++) {
        for (int i = 0; i < n; i++) {
            dp[t][i] = NEG;
        }
    }

    // 시작: c[i] == 0 인 사냥터는 시간 0에 경험치 0으로 시작 가능
    for (int i = 0; i < n; i++) {
        if (c[i] == 0) dp[0][i] = 0;
    }

    // DP 진행
    for (int t = 0; t < T; t++) {
        for (int i = 0; i < n; i++) {
            long long curExp = dp[t][i];
            if (curExp == NEG) continue; // 도달 불가능 상태는 스킵

            // 1. 현재 사냥터에서 1분 더 사냥
            if (t + 1 <= T) {
                long long nextExp = curExp + e[i];
                dp[t + 1][i] = max(dp[t + 1][i], nextExp);
            }

            // 2. 다른 사냥터로 이동
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                int d = travelTime[i][j];
                int nt = t + d;
                if (nt > T) continue;

                // 도착해서 j에 입장할 때 경험치 조건
                if (curExp >= c[j]) {
                    dp[nt][j] = max(dp[nt][j], curExp);
                }
            }
        }
    }

    // 시간 T에 있을 수 있는 최대 경험치
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        if (dp[T][i] > ans) ans = dp[T][i];
    }
    return ans;
}

int main() {
    int n, T;
    static int c[MAXN];
    static int e[MAXN];
    static int travelTime[MAXN][MAXN];

    scanf("%d %d", &n, &T);

    for (int i = 0; i < n; i++) {
        scanf("%d %d", &c[i], &e[i]);
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &travelTime[i][j]);
        }
    }

    long long answer = maplestory(n, T, c, e, travelTime);
    printf("%lld\n", answer);

    return 0;
}