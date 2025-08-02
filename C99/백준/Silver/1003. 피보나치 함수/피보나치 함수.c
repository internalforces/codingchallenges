#include <stdio.h>

int main() {
    int T;
    int a[100];
    int dp0[41] = {0};
    int dp1[41] = {0};

    dp0[0] = 1;
    dp1[0] = 0;

    dp0[1] = 0;
    dp1[1] = 1;

    for (int i = 2; i <= 40; i++) {
        dp0[i] = dp0[i - 1] + dp0[i - 2];
        dp1[i] = dp1[i - 1] + dp1[i - 2];
    }

    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        scanf("%d", &a[i]);
    }

    for (int i = 0; i < T; i++) {
        printf("%d %d\n", dp0[a[i]], dp1[a[i]]);
    }

    return 0;
}