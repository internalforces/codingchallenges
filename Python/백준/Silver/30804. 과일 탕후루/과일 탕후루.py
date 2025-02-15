from collections import defaultdict
import sys

def tang2hurururu(N, S):
    left = 0  
    max_length = 0  
    fruit_count = defaultdict(int)  
    now_fruits = 0  

    for right in range(N):  
        if fruit_count[S[right]] == 0:  
            now_fruits += 1
        fruit_count[S[right]] += 1  

        
        while now_fruits > 2:
            fruit_count[S[left]] -= 1  
            if fruit_count[S[left]] == 0:  
                now_fruits -= 1
            left += 1  

        
        max_length = max(max_length, right - left + 1)

    return max_length  


N = int(sys.stdin.readline().strip())  
S = list(map(int, sys.stdin.readline().split()))  


print(tang2hurururu(N, S))