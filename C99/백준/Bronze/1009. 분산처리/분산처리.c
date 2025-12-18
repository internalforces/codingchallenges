#include <stdio.h>
#include <math.h>

int pow_a_b(int a, int b){
    int result = 1;
    a = a % 10;

    for(int i = 0; i < b; i++){
        result = (result * a) % 10;
    }

    return result == 0 ? 10 : result;
}

int main(){
    int t;
    scanf("%d", &t);

    int a, b;

    for(int i = 0; i < t; i++){
        scanf("%d %d", &a, &b);
        printf("%d\n", pow_a_b(a, b));
    }

    return 0;
}