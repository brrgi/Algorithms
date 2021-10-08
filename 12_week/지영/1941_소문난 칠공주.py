import sys
from collections import deque
input = sys.stdin.readline


SOM = 'S'
YEON = 'Y'
SIZE = 5
BREAK = 7

maps = [input() for _ in range(SIZE)] 

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


princess = deque()
ans = set()
visited = [[False] * SIZE for _ in range(SIZE)]

def backtrack(n, cnt):
    if (cnt + (7 - n) < 4):
        return

    if n == BREAK:
        if cnt >= 4:
            temp = list(princess)
            temp.sort()
            temp = tuple(temp)
            ans.add(temp)
        return

    possible = set()
    for node in princess:
        for i in range(4):
            nx = node[0] + dr[i]
            ny = node[1] + dc[i]
            if nx < 0 or ny < 0 or nx == 5 or ny == 5 or visited[nx][ny]: continue
 
            possible.add((nx,ny))

    for node in possible:

        visited[node[0]][node[1]] = True
        princess.append(node)

        print(princess, cnt)
        if maps[node[0]][node[1]] == SOM:
            backtrack(n+1, cnt+1)
        else:
            backtrack(n+1, cnt)

        princess.pop();
        visited[node[0]][node[1]] = False


for i in range(5):
    for j in range(5):
        if maps[i][j] == SOM:
            visited[i][j] = True
            princess.append((i,j))
            backtrack(1,1)
            princess.popleft()

print(len(ans))