#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_N 12

typedef struct {
    int neighbors[MAX_N];
    int count;
} Node;

Node graph[MAX_N];
int n;
int colors[MAX_N];
int min_colors;

int is_safe(int node, int color) {
    for (int i = 0; i < graph[node].count; i++) {
        int neighbor = graph[node].neighbors[i];
        if (colors[neighbor] == color) {
            return 0;
        }
    }
    return 1;
}

void backtrack(int node, int num_colors) {
    if (node == n) {
        if (num_colors < min_colors) {
            min_colors = num_colors;
        }
        return;
    }

    // 가지치기
    if (num_colors >= min_colors) {
        return;
    }

    // 기존 색 중 하나를 사용하는 경우
    for (int c = 0; c < num_colors; c++) {
        if (is_safe(node, c)) {
            colors[node] = c;
            backtrack(node + 1, num_colors);
            colors[node] = -1;
        }
    }

    // 새로운 색을 사용하는 경우
    if (num_colors + 1 < min_colors) {
        colors[node] = num_colors;
        backtrack(node + 1, num_colors + 1);
        colors[node] = -1;
    }
}

int create_graph(int N, double Coordinates[][2]){
    n = N;

    // 초기화
    for (int i = 0; i < n; i++){
        graph[i].count = 0;
        colors[i] = -1;
    }

    // 그래프 구성: 거리가 20 이하인 점들을 연결
    for (int i = 0; i < n; i++){
        for (int j = i + 1; j < n; j++){
            double dx = Coordinates[i][0] - Coordinates[j][0];
            double dy = Coordinates[i][1] - Coordinates[j][1];
            double dist = sqrt(dx * dx + dy * dy);

            // 거리가 20.0 이하면 연결 (작은 여유값 추가)
            if(dist < 20.0 + 1e-9){
                graph[i].neighbors[graph[i].count++] = j;
                graph[j].neighbors[graph[j].count++] = i;
            }
        }
    }

    // 백트래킹으로 최소 색 개수 찾기
    min_colors = n;

    backtrack(0, 0);

    return min_colors;
}

int main(){
    int n;
    scanf("%d", &n);

    double Coordinates[n][2];

    for (int i = 0; i < n; i++){
        scanf("%lf %lf", &Coordinates[i][0], &Coordinates[i][1]);
    }

    printf("%d\n", create_graph(n, Coordinates));
    return 0;
}