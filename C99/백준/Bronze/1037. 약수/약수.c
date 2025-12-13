#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b){
    return (*(int *)a - *(int *)b);
}

int find_number_of_divisors(int *divisors, int n){
    qsort(divisors, n, sizeof(int), compare);
    return divisors[0] * divisors[n - 1];
}

int main(){
    int n;
    scanf("%d", &n);

    int *divisors = (int *)malloc(sizeof(int) * n);

    for(int i = 0; i < n; i++){
        scanf("%d", &divisors[i]);
    }

    int result = find_number_of_divisors(divisors, n);
    printf("%d\n", result);

    free(divisors);
    return 0;
}