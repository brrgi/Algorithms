import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline
m, n=map(int,input().split())
dir=[(1,0),(-1,0),(0,1),(0,-1)]

maps=[[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    t=input()
    for j in range(n):
        maps[i][j]=int(t[j])
# print(maps)

visit=[[0 for _ in range(n)] for _ in range(m)]

def dfs(row, col):
    global visit
    visit[row][col]=1
    for i in dir:
        newRow=row+i[0]
        newCol=col+i[1]
        if 0<=newRow<m and 0<=newCol<n:
            if maps[newRow][newCol]==0 and visit[newRow][newCol]==0:
                dfs(newRow, newCol)

for i in range(n):
    if maps[0][i]==0 and visit[0][i]==0:
        dfs(0, i)   #row , col

if visit[m-1].count(1)!=0:
    print("YES")
else:
    print("NO")
