#include <stdio.h>

int main(void) {
    int t;
    scanf("%d", &t);
    getchar();

    while (t-- > 0) {
        double x;
        scanf("%lf", &x);

        int ch;
        while ((ch = getchar()) != '\n') {
            if (ch == ' '){
                continue;
            }
            if (ch == '@'){
                x *= 3;
            }
            else if (ch == '%'){
                x += 5;
            }
            else if (ch == '#'){
                x -= 7;
            }
        }
        printf("%.2f\n", x);
    }
    return 0;
}
