#include <stdio.h>

double power_yeod(int x1, int x2, int a, int b, int c){
    double X1 = x1, X2 = x2;
    return ((a/3.0)*X2*X2*X2 + (b/2.0)*X2*X2 + (double)c*X2)
         - ((a/3.0)*X1*X1*X1 + (b/2.0)*X1*X1 + (double)c*X1);
}

int main(){
    int x1, x2;
    int a, b, c, d, e;

    scanf("%d %d", &x1, &x2);
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);

    int B = b-d;
    int C = c-e;

    int result = power_yeod(x1, x2, a, B, C);
    printf("%d\n", result);
    return 0;
}