#include <stdio.h>

int main(){
    char str[1000001];
    char result;

    scanf("%s", str);
    int count[26] = {0,};
    for(int i = 0; str[i] != '\0'; i++){
        if(str[i] >= 'a'){
            count[str[i] - 'a']++;
        }
        else{
            count[str[i] - 'A']++;
        }
    }

    int max = 0;

    for(int i = 0; i < 26; i++){
        if(count[i] == max){
            result = '?';
        }
        else if(count[i] > max){
            max = count[i];
            result = i + 'A';

        }
    }

    printf("%c\n", result);

    return 0;
}