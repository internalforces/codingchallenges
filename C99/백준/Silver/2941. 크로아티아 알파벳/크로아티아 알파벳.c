#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int CroatianAlphabetCount(char *s){
    int count = 0;
    int i = 0;

    while (i < strlen(s)){
        if (s[i] == 'c'){
            if (s[i+1] == '='){
                i++;
            }
            else if (s[i+1] == '-'){
                i++;
            }
        }
        else if (s[i] == 'd'){
            if (s[i+1] == '-'){
                i++;
            }
            else if(s[i+1] == 'z' && s[i+2] == '='){
                i += 2;
            }
        }
        else if(s[i] == 'z'){
            if (s[i+1] == '='){
                i++;
            }
        }
        else if(s[i] == 'l'){
            if(s[i+1] == 'j'){
                i++;
            }
        }
        else if(s[i] == 'n'){
            if(s[i+1] == 'j'){
                i++;
            }
        }
        if (s[i] == 's'){
            if (s[i+1] == '='){
                i++;
            }
        }

        count++;
        i++;

    }

    return count;
}

int main(){
    char *s = (char *)malloc(101 * sizeof(char));
    scanf("%s", s);

    int result = CroatianAlphabetCount(s);
    printf("%d\n", result);

    free(s);
    
    return 0;
}   