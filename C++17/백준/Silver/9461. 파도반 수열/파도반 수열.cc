#include <stdio.h>

int main() {
    int t, n;
    long long dp[101] = {0};
    
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 1;

    for (int i = 4; i <= 100; i++) {
        dp[i] = dp[i - 2] + dp[i - 3];
    }

    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        scanf("%d", &n);
        printf("%lld\n", dp[n]);
    }

    return 0;
}