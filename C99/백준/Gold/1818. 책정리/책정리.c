#include <stdio.h>

int binary_search(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;
    int result = size;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] >= target) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return result;
}

int main(){
    int n;
    scanf("%d", &n);

    int arr[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    int lis[n];
    int lis_length = 0;
    
    lis[0] = arr[0];
    lis_length = 1;
    
    for(int i = 1; i < n; i++){
        if(lis[lis_length - 1] < arr[i]){
            lis[lis_length] = arr[i];
            lis_length++;
        } else {
            int idx = binary_search(lis, lis_length, arr[i]);
            lis[idx] = arr[i];
        }
    }
    
    printf("%d\n", n - lis_length);
    
    return 0;
}