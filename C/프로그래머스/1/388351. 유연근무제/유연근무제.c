#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// schedules_len은 배열 schedules의 길이입니다.
// timelogs_rows는 2차원 배열 timelogs의 행 길이, timelogs_cols는 2차원 배열 timelogs의 열 길이입니다.
int solution(int schedules[], int schedules_len, int** timelogs, int timelogs_rows, int timelogs_cols, int startday) {
    int answer = 0;

    for (int i = 0; i < schedules_len; i++) {
        schedules[i] += 10;
        if (schedules[i] % 100 >= 60) {
            schedules[i] = ((schedules[i] / 100) + 1) * 100 + (schedules[i] % 100) - 60;
        }
    }

    int time = 0;
    
    while (time < schedules_len) {
        int sinchangsup = startday;
        int i = 0;
        
        while (i < timelogs_cols) {
            if (schedules[time] < timelogs[time][i]) {
                if (sinchangsup % 7 != 0 && sinchangsup % 7 != 6) {
                    break;
                }
            }
            sinchangsup += 1;
            i++;
        }

        if (i == timelogs_cols) {
            answer++;
        }

        time++;
    }

    return answer;
}