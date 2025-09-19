#include <stdio.h>
#include <string.h>

void word_reversed(char *word,char *word_reverse){
    int len = strlen(word);

    for (int i = 0; i < len; i++){
        word_reverse[i] = word[len - 1 - i];
    }
    word_reverse[len] = '\0';
}

int main(){

    char word[101];
    char word_reverse[101];

    scanf("%100s", word);
    word_reversed(word, word_reverse);
    
    if(strcmp(word, word_reverse) == 0){
        printf("1");
    } else {
        printf("0");
    }
    return 0;
}