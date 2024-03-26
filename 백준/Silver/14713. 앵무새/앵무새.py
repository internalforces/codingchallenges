from collections import deque

n = int(input())
q = []
for _ in range(n):
    q.append(deque(input().split()))

cq = deque(input().split())

while cq:
    temp = cq.popleft()
    cnt = 0

    for queue in q:
        if queue[0] == temp:
            queue.popleft()
            if not queue:
                q.remove(queue)
            cnt = 1
            break

    if cnt == 0:
        print('Impossible')
        exit(0)

if q:
    print('Impossible')
else:
    print('Possible')
