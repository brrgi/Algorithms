from collections import deque

n, m = map(int, input().split())
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
maps = []
ceiling = 0
max_v = 0
check=1
res=1
for water in range(n):
    ipt = list(map(int, input()))
    ceiling = max(ceiling, max(ipt))
    maps.append(ipt)

def bfs(row, col, num):
    queue=deque()
    queue.append((row, col))
    check=1
    cnt=1
    visit[row][col]=1

    while queue:
        data=queue.popleft()
        for r, c in dir:
            new_r=data[0]+r
            new_c=data[1]+c
            if 0 <= new_r < n and 0 <= new_c < m:
                if visit[new_r][new_c] == 0 and maps[new_r][new_c] <= num:
                    visit[new_r][new_c] = 1
                    cnt += 1
                    queue.append((new_r, new_c))
            else:
                check = 0
    if check==1:
        return cnt
    else:
        return 0



for water in range(1, 9):
    visit = [[0] * (m) for _ in range(n)]
    # print("------------------------")
    for ro in range(n):
        for co in range(m):
            if visit[ro][co] == 0 and maps[ro][co] <= water:
                max_v+=bfs(ro, co, water)
print(max_v)