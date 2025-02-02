from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])
    # queue = [1]
    visited[start] = True
    # visited = [F, T, F, F, F, ... , F]

    while queue:
        v = queue.popleft()
        # v = 1 / queue = []
        print(v, end=' ')
        # 1 
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # queue = [2, 3, 8]
                visited[i] = True
                # visited = [F, T, T, T, ... , T]
                
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)

# queue 변화 
# 1 -> 2, 3, 8, -> 3, 8, 7 -> 8, 7, 4, 5 -> 4, 5, 7, 6 -> ...


