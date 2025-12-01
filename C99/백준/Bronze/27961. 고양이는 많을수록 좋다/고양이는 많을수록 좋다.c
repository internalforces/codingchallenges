#include <stdio.h>

long min_cat(long n){
    long count = 0;
    long cat = 0;

    while(cat < n){
        if(cat == 0) {
            cat = 1;
        }
        else {
            cat += cat;
        }
        count++;
    }
    return count;
}

int main(){
    long n;
    scanf("%ld", &n);

    printf("%ld\n", min_cat(n));
    return 0;
}