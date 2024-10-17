import sys
sys.stdin = open('2. input.txt')

def dfs(g, v, visited):
    visited[v] = True # 방문한경우에
    print(v, end=' ') # 방문한 정점 v를 공백으로 한칸 띄워서 출력
    for i in sorted(g[v]): 
        if not visited[i]:
            dfs(g, i, visited)


N, M, V = map(int, input().split()) # N = 정점 개수, M = 간선의 개수, V = 시작 정점 번호
visited = [False] * (N+1) # visited 배열도 1부터 시작할꺼기 때문에 out of range가 안생기게 N+1까지
g = [[] for _ in range(N+1)] # g는 간선을 저장할 그래프를 만들 예정
for _ in range(M):
    u, v = map(int,input().split()) # 정점 두개를 입력 받는다.
    g[u].append(v)
    g[v].append(u) # 무향 그래프는 양방향으로 추가한다. (1,2) -> g[1]에 2 추가 / g[2]에 1추가 
                   # -> g = [[],[2],[1]]
# print(g) # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]] -> 0번 부터가 아니라 1번 부터니까

dfs(g, V, visited)
