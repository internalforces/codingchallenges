#include <stdio.h>

int team_count(int n, int m, int k){
    int teams = 0;

    while(1){
        n -= 2;
        m -= 1;
        if(n < 0 || m < 0 || n + m < k){
            break;
        }
        teams++;
    }
    return teams;
}

int main(){
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);

    printf("%d\n", team_count(n, m, k));

    return 0;
}