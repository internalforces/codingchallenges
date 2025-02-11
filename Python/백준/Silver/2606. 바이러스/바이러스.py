import sys

def dfs(node, visited, graph):
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, visited, graph)
    return len(visited) - 1  

input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())

graph = {}
for _ in range(m):
    u, v = map(int, input().strip().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  

visited_set = set()
print(dfs(1, visited_set, graph))