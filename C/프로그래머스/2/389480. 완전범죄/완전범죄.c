#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int solution(int** info, size_t info_rows, size_t info_cols, int n, int m) {
    // dp[b] = B의 흔적이 b개일 때 A의 최소 흔적
    int* dp = (int*)malloc(m * sizeof(int));
    int* new_dp = (int*)malloc(m * sizeof(int));
    
    // 초기화
    for(int i = 0; i < m; i++) {
        dp[i] = INT_MAX;
    }
    dp[0] = 0;  // 처음에는 흔적이 없음
    
    // 각 물건 처리
    for(int i = 0; i < info_rows; i++) {
        int a_trace = info[i][0];  // A가 훔칠 때 흔적
        int b_trace = info[i][1];  // B가 훔칠 때 흔적
        
        // new_dp 초기화
        for(int j = 0; j < m; j++) {
            new_dp[j] = INT_MAX;
        }
        
        // 현재 가능한 모든 상태에서
        for(int b = 0; b < m; b++) {
            if(dp[b] == INT_MAX) continue;  // 불가능한 상태
            
            // 경우 1: A가 이 물건을 훔치는 경우
            int new_a = dp[b] + a_trace;
            if(new_a < n) {  // A가 안 잡히는 경우만
                if(new_dp[b] > new_a) {
                    new_dp[b] = new_a;
                }
            }
            
            // 경우 2: B가 이 물건을 훔치는 경우
            int new_b = b + b_trace;
            if(new_b < m) {  // B가 안 잡히는 경우만
                if(new_dp[new_b] > dp[b]) {
                    new_dp[new_b] = dp[b];
                }
            }
        }
        
        // dp 갱신
        memcpy(dp, new_dp, m * sizeof(int));
    }
    
    // 최소값 찾기 (B < m인 모든 경우 중)
    int answer = INT_MAX;
    for(int b = 0; b < m; b++) {
        if(dp[b] < answer) {
            answer = dp[b];
        }
    }
    
    // 메모리 해제
    free(dp);
    free(new_dp);
    
    // 불가능하면 -1 반환
    return (answer == INT_MAX) ? -1 : answer;
}