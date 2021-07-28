import sys
from collections import deque

input = sys.stdin.readline

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())
maps = []
visit = [[[0 for _ in range(64)] for _ in range(m)] for _ in range(n)]
result = -1
queue = deque()


def init_map():
    for i in range(n):
        t = input().rstrip()
        maps.append(t)
    for i in range(n):
        for j in range(m):
            if maps[i][j] == '0':
                queue.append((i, j, 0))  # (row, col, visit)
init_map()

while queue:
    data = queue.popleft()
    row = data[0]
    col = data[1]
    z = data[2]

    if maps[row][col] == '1':
        result = visit[row][col][z]                                 #출구 중 아무거나 도착하면 끝
        break

    for d in dir:
        new_row = row + d[0]
        new_col = col + d[1]
        zz = z

        if 0 <= new_row < n and 0 <= new_col < m:
            cur = maps[new_row][new_col]
            if 97 <= ord(cur) < 123:  # 소문자 key
                zz |= (1 << (ord(cur) - 97))                        #열쇠를 표현하는 bit masking
            elif 65 <= ord(cur) < 91:  # 대문자 문
                if not zz & (1 << (ord(cur) - 65)):                 #대문자 문을 만났을 때, 열쇠가 없으면
                    continue
            if not visit[new_row][new_col][zz] and cur != '#':      #zz열쇠의 상태일 때 방문 x, 그리고 벽이 아닐 때
                queue.append((new_row, new_col, zz))
                visit[new_row][new_col][zz] = visit[row][col][z] + 1

print(result)
