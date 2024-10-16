import sys
sys.stdin = open('2. input.txt')

N, M = map(int, input().split())

'''
질문: 순열과 조합의 함수에서 들어가는 인자의 갯수가 왜 다른가요?
'''

num_list = []
for i in range(1, N+1):
    num_list.append(i)
visited = [False for _ in range(N)]
ans = []
'''
# 순열
def dfs(depth):
    if depth == M: # M개가 되면 출력
        print(*ans)
        return
    for i in range(N): # 0~N-1까지
        if visited[i] == False: # 입력되지 않았으면
            visited[i] == True # 입력을 하겠다고 하고
            ans.append(num_list[i]) # 정답 리스트에 추가
            dfs(depth+1) # M개가 될때까지 + 1 해서 반복
            ans.pop() # 다음을 위해 pop해서 돌아간다
            visited[i] = False #그리고 방문하지 않았다고 다시 바꾼다.
dfs(0)
'''

# 조합
def dfs2(start, depth):
    if depth == M:
        print(*ans)
        return
    for i in range(N-1, start-1, -1):
        ans.append(num_list[i])
        dfs2(i, depth+1)
        ans.pop()
dfs2(0, 0)

#별짓을 다해도 모르겠음!