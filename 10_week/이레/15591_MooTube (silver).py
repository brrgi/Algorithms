import sys
from collections import deque

n, w = map(int, input().split())
go=[[] for _ in range(n+1)]

for i in range(n - 1):
    p, q, r = map(int, input().split())  # p와q가 r로 서로 연결되어 있음
    go[p].append([q, r])    #가는 방향, 거리
    go[q].append([p, r])


for i in range(w):
    k, v = map(int, input().split())
    queue = deque()
    queue.append([v, sys.maxsize])
    visit=[0 for _ in range(n+1)]
    visit[v]=1
    while queue:
        data=queue.popleft()
        for i in go[data[0]]:
            next, length=i[0], min(i[1], data[1])
            if visit[next]==0 and length>=k:
                visit[next]=1
                queue.append([next,length])
    print(visit.count(1)-1)