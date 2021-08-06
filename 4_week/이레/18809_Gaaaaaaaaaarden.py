import sys
from copy import deepcopy
from collections import deque
input=sys.stdin.readline
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m, g, r = map(int, input().split())
maps = []
ans=0
for i in range(n):
    maps.append(list(map(int, input().split())))

yellow = []
cases = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            yellow.append((i, j))

start = '0' * len(yellow)


def make_combination(strs, red, green, idx):
    if red + green == r + g:
        cases.append(strs)
        return
    if idx == len(yellow):
        return

    make_combination(strs, red, green, idx + 1)
    strs = strs[:idx] + '1' + strs[idx + 1:]
    if red < r:
        make_combination(strs, red + 1, green, idx + 1)
    strs = strs[:idx] + '2' + strs[idx + 1:]
    if green < g:
        make_combination(strs, red, green + 1, idx + 1)
make_combination(start, 0, 0, 0)

for case in cases:
    new_maps = deepcopy(maps)
    res=0
    visit = [[0 for _ in range(m)] for _ in range(n)]
    color = [[0 for _ in range(m)] for _ in range(n)]
    r_queue = deque()
    g_queue = deque()

    for i in range(len(case)):
        if case[i] == '1':  # red
            r_queue.append(yellow[i])
            visit[yellow[i][0]][yellow[i][1]] = 1
            color[yellow[i][0]][yellow[i][1]] = 1
        elif case[i] == '2':  # green
            g_queue.append(yellow[i])
            visit[yellow[i][0]][yellow[i][1]] = 1
            color[yellow[i][0]][yellow[i][1]] = 2

    while r_queue or g_queue:
        if r_queue:
            for _ in range(len(r_queue)):
                r_data = r_queue.popleft()
                if new_maps[r_data[0]][r_data[1]]==3:
                    continue
                for d in dir:
                    r_row = r_data[0] + d[0]
                    r_col = r_data[1] + d[1]
                    if 0<=r_row<n and 0<=r_col<m and visit[r_row][r_col]==0:
                        if new_maps[r_row][r_col]==1 or new_maps[r_row][r_col]==2:
                            visit[r_row][r_col]=visit[r_data[0]][r_data[1]]+1
                            color[r_row][r_col] = 1
                            r_queue.append((r_row, r_col))
        if g_queue:
            for _ in range(len(g_queue)):
                g_data = g_queue.popleft()
                for d in dir:
                    g_row = g_data[0] + d[0]
                    g_col = g_data[1] + d[1]
                    if 0 <= g_row < n and 0 <= g_col < m:
                        if visit[g_row][g_col] == 0:
                            if new_maps[g_row][g_col] == 1 or new_maps[g_row][g_col] == 2:
                                visit[g_row][g_col] = visit[g_data[0]][g_data[1]] + 1
                                color[g_row][g_col] = 2
                                g_queue.append((g_row, g_col))
                        elif visit[g_row][g_col]==visit[g_data[0]][g_data[1]] + 1:
                            if color[g_row][g_col] == 1 and new_maps[g_row][g_col]!=3:
                                new_maps[g_row][g_col]=3
                                res+=1

    ans=max(ans, res)
print(ans)