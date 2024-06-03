import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    n_a, n_b, cost = map(int, input().split())
    graph[n_a].append((n_b, cost))
    graph[n_b].append((n_a, cost))

v1, v2 = map(int, input().split())

def dijkstra(start, target):
    distance = [INF] * (n + 1)
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, n_now = heapq.heappop(pq)

        if n_now == target:
            return distance[target]

        if distance[n_now] < dist:
            continue

        for i in graph[n_now]:
            c = dist + i[1]
            if c < distance[i[0]]:
                distance[i[0]] = c
                heapq.heappush(pq, (c, i[0]))

    return distance[target]


path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

result = min(path1, path2)

if result >= INF:
    print(-1)
else:
    print(result)