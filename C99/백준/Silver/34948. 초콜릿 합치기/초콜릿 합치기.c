#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int h;
    int w;
} Rectangle;

int compare(const void *a, const void *b) {
    Rectangle *rectA = (Rectangle *)a;
    Rectangle *rectB = (Rectangle *)b;
    if(rectA->h > rectB->h) {
        return 1;
    }
    if(rectA->h < rectB->h) {
        return -1;
    }
    return 0;
}


int main(){
    int n;
    scanf("%d", &n);

    Rectangle *rects = (Rectangle *)malloc(n * sizeof(Rectangle));

    for(int i = 0; i < n; i++){
        scanf("%d", &rects[i].h);
    }
    for(int i = 0; i < n; i++){
        scanf("%d", &rects[i].w);
    }

    qsort(rects, n, sizeof(Rectangle), compare);

    long long maxArea = 0;
    long long widthSum = 0;

    for(int i = n - 1; i >= 0; i--) {
        widthSum += rects[i].w;

        if(i == 0 || rects[i].h != rects[i-1].h) {
            long long area = (long long)rects[i].h * widthSum;
            if(area > maxArea) {
                maxArea = area;
            }
        }
    }

    printf("%lld\n", maxArea);

    free(rects);
    return 0;
}