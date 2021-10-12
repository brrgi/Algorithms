M, N = map(int, input().split())

graph = [[1] * M for _ in range(M)]
for _ in range(N):
    f, s, t = map(int, input().split())
    li = [0] * f + [1] * s + [2] * t
    
    cnt = 0
    for row in range(M-1, -1, -1):
        graph[row][0] += li[cnt]
        cnt += 1
    
    for col in range(1, M):
        graph[0][col] += li[cnt]
        cnt += 1

for row in range(1, M):
    for col in range(1, M):
        graph[row][col] = max([graph[row][col-1], graph[row-1][col], graph[row-1][col-1]])

for elm in graph:
    print(*elm)