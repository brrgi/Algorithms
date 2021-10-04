n, K = map(int, input().split())        #행성의 개수 n과 발사되는 행성의 위치 k
inf = 100000000
s=[list(map(int, input().split())) for _ in range(n)]
result=inf
visit=[0 for _ in range(n)]
visit[K]=1
def dfs(a, number, value):
    global result

    if number == n:
        result = min(value, result)
        return

    for i in range(n):
        if visit[i]==0:
            visit[i] = 1
            dfs(i, number + 1, value + s[a][i])
            visit[i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            s[i][j]=min(s[i][j], s[i][k]+s[k][j])


dfs(K, 1, 0)
print(result)
