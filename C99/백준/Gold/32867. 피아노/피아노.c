#include <stdio.h>

int piano(int n, int k, int *a){
    int count = 0;
    int min = a[0];
    int max = a[0];

    for (int i = 1; i < n; i++){
        if (a[i] < min){
            min = a[i];
        }
        else if(a[i] > max){
            max = a[i];
        }

        if (max - min >= k){
            count++;
            min = a[i];
            max = a[i];
        }
    }
    return count;
}


int main(){
    int n, k;
    scanf("%d %d", &n, &k);
    int a[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }

    printf("%d\n", piano(n, k, a));

    return 0;
}