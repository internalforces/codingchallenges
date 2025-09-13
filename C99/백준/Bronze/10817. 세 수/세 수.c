#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    int numbers[3];

    for (int i = 0; i < 3; i++) {
        scanf("%d", &numbers[i]);
    }

    qsort(numbers, 3, sizeof(int), compare);

    printf("%d\n", numbers[1]);

    return 0;
}