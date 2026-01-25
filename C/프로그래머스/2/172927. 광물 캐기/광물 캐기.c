
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    size_t start;
    size_t len;
    int stone_cost;
} Group;

static int cmp_group(const void *a, const void *b) {
    const Group *ga = (const Group *)a;
    const Group *gb = (const Group *)b;
    return gb->stone_cost - ga->stone_cost;
}


// picks_len은 배열 picks의 길이입니다.
// minerals_len은 배열 minerals의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(int picks[], size_t picks_len, const char* minerals[], size_t minerals_len) {
    int answer = 0;

    int totalPicks = picks[0] + picks[1] + picks[2];
    size_t maxMine = (size_t)totalPicks * 5;
    
    if (minerals_len > maxMine) {
        minerals_len = maxMine;
    }
    if (minerals_len == 0) {
        return 0;
    }

    int *dia_piro   = (int *)malloc(sizeof(int) * minerals_len);
    int *iron_piro  = (int *)malloc(sizeof(int) * minerals_len);
    int *stone_piro = (int *)malloc(sizeof(int) * minerals_len);

    for (size_t i = 0; i < minerals_len; i++) {
        dia_piro[i] = 1;

        if (strcmp(minerals[i], "diamond") == 0) {
            iron_piro[i] = 5;
        }
        else {
            iron_piro[i] = 1;
        }

        if (strcmp(minerals[i], "diamond") == 0) {
            stone_piro[i] = 25;
        }
        else if (strcmp(minerals[i], "iron") == 0) {
            stone_piro[i] = 5;
        }
        else {
            stone_piro[i] = 1;
        }
    }

    size_t gCount = (minerals_len + 4) / 5;
    Group *groups = (Group *)malloc(sizeof(Group) * gCount);

    for (size_t g = 0; g < gCount; g++) {
        size_t start = g * 5;
        size_t len = 5;
        if (start + len > minerals_len) len = minerals_len - start;

        int cost = 0;
        for (size_t k = 0; k < len; k++) {
            cost += stone_piro[start + k];
        }

        groups[g].start = start;
        groups[g].len = len;
        groups[g].stone_cost = cost;
    }

    qsort(groups, gCount, sizeof(Group), cmp_group);

    for (size_t g = 0; g < gCount; g++) {
        size_t start = groups[g].start;
        size_t len = groups[g].len;

        if (picks[0] > 0) {
            picks[0]--;
            for (size_t k = 0; k < len; k++) {
                answer += dia_piro[start + k];
            }
        } else if (picks[1] > 0) {
            picks[1]--;
            for (size_t k = 0; k < len; k++) {
                answer += iron_piro[start + k];
            }
        } else if (picks[2] > 0) {
            picks[2]--;
            for (size_t k = 0; k < len; k++) {
                answer += stone_piro[start + k];
            }
        } else {
            break;
        }
    }

    free(dia_piro);
    free(iron_piro);
    free(stone_piro);
    free(groups);

    return answer;
}
