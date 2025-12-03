#include <stdio.h>

int stack_fuc(int n, int commands[][2]) {
    int *stack = malloc(sizeof(int) * n);
    int top = -1;

    for (int i = 0; i < n; i++) {
        int cmd = commands[i][0];
        if (cmd == 1) {
            int value = commands[i][1];
            stack[++top] = value;
        } else if (cmd == 2) {
            if (top == -1) {
                printf("-1\n");
            } else {
                printf("%d\n", stack[top--]);
            }
        } else if (cmd == 3) {
            printf("%d\n", top + 1);
        } else if (cmd == 4) {
            printf("%d\n", top == -1 ? 1 : 0);
        } else if (cmd == 5) {
            if (top == -1) {
                printf("-1\n");
            } else {
                printf("%d\n", stack[top]);
            }
        }
    }
    return 0;
}

int main() {
    int n;
    scanf("%d", &n);
    int (*commands)[2] = malloc(sizeof(int) * 2 * n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &commands[i][0]);
        if (commands[i][0] == 1) {
            scanf("%d", &commands[i][1]);
        }
    }

    stack_fuc(n, commands);
    return 0;
}