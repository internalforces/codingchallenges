#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define OFFSET 4000
#define RANGE 8001

// 산술평균 구하기
int avg(int* arr, int size) {
    long long sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return (int)round((double)sum / (double)size);
}

// 정렬하기
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

// 최빈값 (여러 개면 두 번째로 작은 값)
int mode(const int *arr, int n) {
    int cnt[RANGE] = {0};

    for (int i = 0; i < n; i++) {
        cnt[arr[i] + OFFSET]++;
    }

    int maxFreq = 0;
    for (int i = 0; i < RANGE; i++) {
        if (cnt[i] > maxFreq) maxFreq = cnt[i];
    }

    int found = 0;
    int result = 0;
    for (int i = 0; i < RANGE; i++) {
        if (cnt[i] == maxFreq) {
            if (found == 0) {
                result = i - OFFSET; // 첫 번째(가장 작은) 최빈값
                found = 1;
            } else {
                result = i - OFFSET; // 두 번째 최빈값
                break;
            }
        }
    }
    return result;
}

int main(){
    int n;
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));
    for(int i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }

    printf("%d\n", avg(arr, n));

    qsort(arr, n, sizeof(int), compare);
    
    printf("%d\n", arr[n/2]);
    printf("%d\n", mode(arr, n));
    printf("%d\n", arr[n-1] - arr[0]);

    free(arr);
    return 0;
}