#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n, long long left, long long right) {

    int size = right - left + 1;

    int* answer = (int*)malloc(sizeof(int) * size);

    int idx = 0;

    for (long long i = left; i <= right; i++) {

        long long row = i / n;
        long long col = i % n;

        if (row > col)
            answer[idx++] = row + 1;
        else
            answer[idx++] = col + 1;
    }

    return answer;
}