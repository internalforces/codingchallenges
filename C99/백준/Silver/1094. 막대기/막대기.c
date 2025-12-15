#include <stdio.h>

int stick_count(int x){
    int count = 0;
    int stick_length = 64;

    while(x > 0){
        if(stick_length <= x){
            x -= stick_length;
            count++;
        }
        stick_length /= 2;
    }

    return count;
}

int main(){
    int x;
    scanf("%d", &x);

    int result = stick_count(x);
    printf("%d\n", result);
    return 0;
}