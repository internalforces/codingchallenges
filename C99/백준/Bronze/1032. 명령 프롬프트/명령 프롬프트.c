#include <stdio.h>
#include <string.h>

void cmd(int n, char s[][51]){
    int len = strlen(s[0]);
    for (int i = 1; i < n; i++){
        for (int j = 0; j < len; j++){
            if (s[0][j] != s[i][j]){
                s[0][j] = '?';
            }
        }
    }
}

int main(){
    int n;
    scanf("%d", &n);
    char s[50][51];

    for(int i=0;i<n;i++){
        scanf("%s", s[i]);
    }

    cmd(n, s);
    printf("%s\n", s[0]);

    return 0;
}