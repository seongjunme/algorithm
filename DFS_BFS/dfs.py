def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
	[1, 2],
    	[0, 3, 4],
    	[0, 5, 6],
    	[1],
    	[1],
    	[2],
    	[2]
]

#각 노드가 방문된 정ㅇ보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9
dfs(graph, 0, visited)