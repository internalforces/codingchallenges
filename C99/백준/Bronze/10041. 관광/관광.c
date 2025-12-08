#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int W, H, N;
    if (scanf("%d %d %d", &W, &H, &N) != 3) return 0;

    int (*P)[2] = (int (*)[2])malloc(sizeof(int) * 2 * N);
    if (!P) return 0;

    for (int i = 0; i < N; i++) {
        scanf("%d %d", &P[i][0], &P[i][1]);
    }

    long long answer = 0;

    for (int i = 0; i < N - 1; i++) {
        int x1 = P[i][0],     y1 = P[i][1];
        int x2 = P[i + 1][0], y2 = P[i + 1][1];

        if (x1 > x2) {
            int tx = x1; x1 = x2; x2 = tx;
            int ty = y1; y1 = y2; y2 = ty;
        }

        int dx = x1 - x2; if (dx < 0) dx = -dx;
        int dy = y1 - y2; if (dy < 0) dy = -dy;

        if (y1 > y2) {
            answer += (long long)dx + (long long)dy;
        } else {
            answer += (dx > dy) ? dx : dy;
        }
    }

    printf("%lld\n", answer);

    free(P);
    return 0;
}