# DFS 예제
# 인접 행렬 : 2차원 배열로 그래프의 연결관계 표현 (연결되지 않은 노드끼리는 무한)
# 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비됨

# 인접 리스트 : 리스트로 그래프간 연결관계를 표현하는 방식
# 정보를 얻는 속도가 느림 (연결된 데이터를 하나씩 확인해야함)

def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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

dfs(graph, 1, visited)
        