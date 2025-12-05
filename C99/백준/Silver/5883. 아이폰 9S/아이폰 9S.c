#include <stdio.h>
#include <stdlib.h>

int iphone_9s(int *n, int *b){
    int *new_b = (int*)malloc(sizeof(int) * (*n));
    int answer = 0;

    int cur = 1, best = 1;
    for (int k = 1; k < *n; k++) {
        if (b[k] == b[k - 1]) cur++;
        else cur = 1;
        if (cur > best) best = cur;
    }
    answer = best;

    int *unique_vals = (int*)malloc(sizeof(int) * (*n));
    int unique_count = 0;

    for (int i = 0; i < *n; i++) {
        int is_duplicate = 0;
        for (int j = 0; j < unique_count; j++) {
            if (b[i] == unique_vals[j]) {
                is_duplicate = 1;
                break;
            }
        }
        if (!is_duplicate) {
            unique_vals[unique_count++] = b[i];
        }
    }

    for (int i = 0; i < unique_count; i++) {
        int remove_val = unique_vals[i];

        int m = 0;
        for (int j = 0; j < *n; j++) {
            if (b[j] != remove_val) {
                new_b[m++] = b[j];
            }
        }

        if (m == 0) continue;

        cur = 1;
        best = 1;
        for (int k = 1; k < m; k++) {
            if (new_b[k] == new_b[k - 1]) cur++;
            else cur = 1;
            if (cur > best) best = cur;
        }

        if (best > answer) answer = best;
    }

    free(unique_vals);
    free(new_b);
    return answer;
}

int main(){
    int n;
    scanf("%d", &n);

    int *b = (int*)malloc(sizeof(int) * n);
    for(int i = 0; i < n; i++){
        scanf("%d", &b[i]);
    }

    printf("%d\n", iphone_9s(&n, b));

    free(b);
    return 0;
}