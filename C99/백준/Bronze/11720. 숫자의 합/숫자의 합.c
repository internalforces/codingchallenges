#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    scanf("%d", &n);
    
    char *numbers = (char *)malloc((n + 1) * sizeof(char));
    scanf("%s", numbers);
    
    int sum = 0;
    for(int i = 0; i < n; i++){
        sum += numbers[i] - '0';
    }
    
    printf("%d\n", sum);
    free(numbers);
    
    return 0;
}