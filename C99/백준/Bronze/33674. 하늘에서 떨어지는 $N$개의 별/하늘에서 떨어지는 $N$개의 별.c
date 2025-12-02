#include <stdio.h>

int kimdsky(int n, int d, int k, const int s[]) {
    int L = 101;
    for (int i = 0; i < n; i++) {
        int can = k / s[i];
        if (can < L) {
            L = can;
        }
    }
    return (d - 1) / L;
}

int main() {
    int n, d, k;
    scanf("%d %d %d", &n, &d, &k);

    int s[101];
    for (int i = 0; i < n; i++) scanf("%d", &s[i]);

    printf("%d\n", kimdsky(n, d, k, s));
    return 0;
}