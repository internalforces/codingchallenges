#include <stdio.h>

int main(){
    int p;
    int n, m;

    scanf("%d", &p);

    int count;
    int a, b;

    for(int i = 0; i < p; i++){
        scanf("%d %d", &n, &m);
        count = 0;
        a = 1;
        b = 1;

        while(1){
            int temp = (a + b) % m;
            a = b;
            b = temp;
            count++;

            if(a == 1 && b == 1){
                break;
            }
        }
        printf("%d %d\n", n, count);
    }
}