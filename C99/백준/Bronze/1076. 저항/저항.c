#include <stdio.h>
#include <string.h>

int get_digit(char color[]){
    if(strcmp(color, "black") == 0) return 0;
    else if(strcmp(color, "brown") == 0) return 1;
    else if(strcmp(color, "red") == 0) return 2;
    else if(strcmp(color, "orange") == 0) return 3;
    else if(strcmp(color, "yellow") == 0) return 4;
    else if(strcmp(color, "green") == 0) return 5;
    else if(strcmp(color, "blue") == 0) return 6;
    else if(strcmp(color, "violet") == 0) return 7;
    else if(strcmp(color, "grey") == 0) return 8;
    else if(strcmp(color, "white") == 0) return 9;
    return 0;
}

long long get_multiplier(char color[]){
    if(strcmp(color, "black") == 0) return 1;
    else if(strcmp(color, "brown") == 0) return 10;
    else if(strcmp(color, "red") == 0) return 100;
    else if(strcmp(color, "orange") == 0) return 1000;
    else if(strcmp(color, "yellow") == 0) return 10000;
    else if(strcmp(color, "green") == 0) return 100000;
    else if(strcmp(color, "blue") == 0) return 1000000;
    else if(strcmp(color, "violet") == 0) return 10000000;
    else if(strcmp(color, "grey") == 0) return 100000000;
    else if(strcmp(color, "white") == 0) return 1000000000;
    return 1;
}

int main(){
    char first_color[20];
    char second_color[20];
    char multiplier_color[20];

    scanf("%s", first_color);
    scanf("%s", second_color);
    scanf("%s", multiplier_color);

    int digit1 = get_digit(first_color);
    int digit2 = get_digit(second_color);
    long long multiplier = get_multiplier(multiplier_color);

    long long result = (digit1 * 10 + digit2) * multiplier;

    printf("%lld\n", result);
    
    return 0;
}