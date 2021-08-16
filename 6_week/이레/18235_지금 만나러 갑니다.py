import sys
from collections import deque

n, a, b = map(int, input().split())
dir=[-1,1]
five_visit=[[0 for _ in range(20)] for _ in range(500001)]
six_visit=[[0 for _ in range(20)] for _ in range(500001)]
five_queue=deque()
six_queue=deque()
ans=sys.maxsize
for i in range(500001):
    for j in range(20):
        five_visit[i][j]=-1
        six_visit[i][j]=-1

def bfs():
    five_queue = deque()
    five_visit[a][0]=0
    five_queue.append((a,0))
    while five_queue:
        now, t = five_queue.popleft()
        d=1<<t

        for i in range(2):
            next=now+(d*dir[i])
            if (1<=next) and next<=n:
                if five_visit[next][t+1]==-1:
                    five_visit[next][t+1]=t+1
                    five_queue.append((next, t+1))


def bfs2():
    global ans
    six_queue = deque()
    six_visit[b][0] = 0
    six_queue.append((b, 0))
    while six_queue:
        now, t = six_queue.popleft()
        d = 1 << t
        if (five_visit[now][t] != -1 and five_visit[now][t] == six_visit[now][t]):
            ans = t
            return

        for i in range(2):
            next = now + (d * dir[i])
            if 1 <= next and next <= n:
                if six_visit[next][t + 1] == -1:
                    six_visit[next][t + 1] = t + 1
                    six_queue.append((next, t + 1))

bfs()
bfs2()
if ans==sys.maxsize:
    ans=-1
print(ans)
