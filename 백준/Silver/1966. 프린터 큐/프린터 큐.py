from collections import deque

N = int(input())


q = deque()
for i in range(N):
    n, choice = map(int, input().split()) #문서 개수, 선택할 수의 자리
    q = deque(map(int, input().split())) #중요도(1~9)
    cnt = 0
    choice_index = choice

    while q:
        if q[0] != max(q):
            q.rotate(-1)
            choice_index = (choice_index - 1) % len(q) #회전 o 위치 다시 잡기
        else:
            if choice_index == 0:
                q.popleft()
                cnt += 1
                break
            else:
                q.popleft()
                cnt += 1
                choice_index -= 1 #회전 x 위치 다시 잡기
                max_num = max(q)
    print(cnt)
'''3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1'''

