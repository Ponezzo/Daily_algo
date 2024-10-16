# 10월 16일

### n과 m(2)
'''
def dfs2(start, depth):
    if depth == M:
        print(*ans)
        return
    for i in range(start, N):
        ans.append(num_list[i])
        dfs2(i+1, depth+1)
        ans.pop()
dfs2(0, 0)
'''

### n과 m(4)
'''
def dfs2(start, depth):
    if depth == M:
        print(*ans)
        return

    for i in range(start, N):
        ans.append(num_list[i])
        dfs2(i, depth+1)
        ans.pop()
dfs2(0, 0)
'''

### n과 m(5)
'''
def dfs2(start, depth):
    if depth == M:
        print(*ans)
        return

    for i in range(start, N):
        ans.append(num_list[i])
        dfs2(i, depth+1)
        ans.pop()
dfs2(0, 0)
# 문제 1. 내림차순이 안됨
# 문제 2. 1~3 다 같은 코드를 돌려쓰는데, (1,1) 과 (9,9)를 제거하는 법을 모르겠다.
'''

### 참고
코드가 쉬워보이는데 이해가 잘 안됨 ㅜ 재귀에 대한 이해가 부족하다고 느낌!
