from collections import deque
dir=[(0,1),(0,-1),(1,0),(-1,0)]
n,m,p=map(int, input().split())
s=list(map(int, input().split()))
maps=[list(input()) for _ in range(n)]
visit=[[[0 for _ in range(m)] for _ in range(n)] for _ in range(p)]
check=0

def make_queue(player):
    queue=deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j]==str(player) and visit[player-1][i][j]==0:
                queue.append([i,j])
    return queue

def bfs(player, number):
    global maps
    global visit
    global check
    start=make_queue(player)

    leng=len(start)
    if leng==0:
        check+=1
        return

    for i in start:
        visit[player-1][i[0]][i[1]]=1

    for i in range(number):
        leng=len(start)
        for j in range(leng):
            data=start.popleft()
            for row, col in dir:
                next_r=data[0]+row
                next_c=data[1]+col
                if 0<=next_r<n and 0<=next_c<m:
                    if maps[next_r][next_c]=='.' and visit[player-1][next_r][next_c]==0:
                        maps[next_r][next_c]=str(player)
                        start.append([next_r, next_c])

while 1:
    check=0
    for i in range(p):
        bfs(i+1,s[i])
    if check==p:

        break

# for i in maps:
#     print(i)

for q in range(p):
    result=0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == str(q+1):
                result+=1
    print(result, end=' ')