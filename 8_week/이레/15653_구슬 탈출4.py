from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
visit = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]  # [n][m][n][m]   red blue
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 아래, 위, 오른쪽, 왼쪽


def find_rbo(row, col):
    red = 0
    blue = 0
    hole = 0
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 'R':
                red = (i, j)
            elif maps[i][j] == 'B':
                blue = (i, j)
            elif maps[i][j] == 'O':
                hole = (i, j)

    return red, blue, hole


def go(direction, row, col):  # 방향, 현재위치
    global n_maps
    start = 1
    while 1:
        new_row = row + direction[0] * start
        new_col = col + direction[1] * start
        if n_maps[new_row][new_col] == '.':  # 갈 수 있으면
            start += 1
        elif n_maps[new_row][new_col] == 'O':  # O빠져 나갈때
            n_maps[row][col] = '.'
            return 0
        else:
            break
    if start != 1:
        n_maps[new_row - direction[0]][new_col - direction[1]] = n_maps[row][col]
        n_maps[row][col] = '.'
    return new_row - direction[0], new_col - direction[1]


red, blue, hole = find_rbo(n, m)
visit[red[0]][red[1]][blue[0]][blue[1]] = 1
queue = deque()
queue.append((red[0], red[1], blue[0], blue[1], maps))
result = 0
r = 0
check = 0
while queue:
    leng = len(queue)
    for i in range(leng):
        red_row, red_col, blue_row, blue_col, nmaps = queue.popleft()
        for d in dir:
            n_maps = deepcopy(nmaps)
            if d == (1, 0):  # 아래
                if red_row > blue_row:
                    new_red = go(d, red_row, red_col)
                    new_blue = go(d, blue_row, blue_col)
                else:
                    new_blue = go(d, blue_row, blue_col)
                    new_red = go(d, red_row, red_col)
            elif d == (-1, 0):  # 위
                if red_row < blue_row:
                    new_red = go(d, red_row, red_col)
                    new_blue = go(d, blue_row, blue_col)
                else:
                    new_blue = go(d, blue_row, blue_col)
                    new_red = go(d, red_row, red_col)
            elif d == (0, 1):  # 오른쪽
                if red_col > blue_col:
                    new_red = go(d, red_row, red_col)
                    new_blue = go(d, blue_row, blue_col)
                else:
                    new_blue = go(d, blue_row, blue_col)
                    new_red = go(d, red_row, red_col)
            elif d == (0, -1):  # 왼쪽
                if red_col < blue_col:
                    new_red = go(d, red_row, red_col)
                    new_blue = go(d, blue_row, blue_col)
                else:
                    new_blue = go(d, blue_row, blue_col)
                    new_red = go(d, red_row, red_col)
            if new_blue == 0:  # 0 다 거르기
                continue
            if new_red == 0:
                check = 1
                continue
            if visit[new_red[0]][new_red[1]][new_blue[0]][new_blue[1]] == 0:
                visit[new_red[0]][new_red[1]][new_blue[0]][new_blue[1]] = 1
                queue.append((new_red[0], new_red[1], new_blue[0], new_blue[1], n_maps))

    r += 1
    if check == 1:
        break
if check == 1:
    result = r
if result == 0:
    print(-1)
else:
    print(result)
