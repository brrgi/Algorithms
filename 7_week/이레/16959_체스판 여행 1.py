'''
    지학이 가진 말  : 나이트, 비숍, 룩
    1. 나이트는 8방향 이동
    2. 비숍과 룩은 범위를 넘을 때까지 이동


    1. 나이트, 비숍, 룩이 갈 수 있는 위치를 queue에 전부 넣어준다. + visit방문 체크
    2. visit방문 체크를 확인하여 방문했으면   -> 다음 숫자로
                                  못했으면 -> queue 계속 돌기
'''
from collections import deque

n = int(input())
maps = []
knight = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]  # 8방향
bishop_default = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
bishop = []
result = 0

dic = dict()

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(n):
        if t[j] == 1:
            start = [i, j]
        dic[t[j]] = [i, j]
    maps.append(t)

for i in range(1, n):
    for j in bishop_default:
        bishop.append((j[0] * i, j[1] * i))


def bfs():
    global result
    queue = deque()
    queue.append(start + [0])
    queue.append(start + [1])
    queue.append(start + [2])

    queue_temp = deque()
    visit_temp = [[[False for _ in range(3)] for _ in range(n)] for _ in range(n)]
    visit = [[[False for _ in range(3)] for _ in range(n)] for _ in range(n)]
    visit[start[0]][start[1]][0] = True  # 나이트
    visit[start[0]][start[1]][1] = True
    visit[start[0]][start[1]][2] = True
    want = maps[start[0]][start[1]] + 1
    print("시작 상태, result :", result)
    for i in visit:
        print(i)
    print("----------------------")
    while queue and want < (n ** 2) + 1:
        cnt = len(queue)
        result += 1
        queue_temp = deque()
        visit_temp = [[[False for _ in range(3)] for _ in range(n)] for _ in range(n)]
        for _ in range(cnt):
            row, col, piece = queue.popleft()

            # step 1 : 나이트 움직이기
            if piece == 0:
                if visit[row][col][1] == False:
                    visit[row][col][1] = True
                    queue.append([row, col, 1])
                if visit[row][col][2] == False:
                    visit[row][col][2] = True
                    queue.append([row, col, 2])
                for i in knight:
                    new_row = row + i[0]
                    new_col = col + i[1]
                    if 0 <= new_row < n and 0 <= new_col < n:
                        if visit[new_row][new_col][0] == False:
                            visit[new_row][new_col][0] = True
                            queue.append([new_row, new_col, 0])

            # step 2 : 룩 움직이기
            elif piece == 1:
                if visit[row][col][0] == False:
                    visit[row][col][0] = True
                    queue.append([row, col, 0])
                if visit[row][col][2] == False:
                    visit[row][col][2] = True
                    queue.append([row, col, 2])
                for i in range(n):
                    if visit[row][i][1] == False:
                        visit[row][i][1] = True
                        queue.append([row, i, 1])
                    if visit[i][col][1] == False:
                        visit[i][col][1] = True
                        queue.append([i, col, 1])

            # step 3 : 비숍 움직이기
            elif piece == 2:
                if visit[row][col][0] == False:
                    visit[row][col][0] = True
                    queue.append([row, col, 0])
                if visit[row][col][1] == False:
                    visit[row][col][1] = True
                    queue.append([row, col, 1])
                for i in bishop:
                    new_row = row + i[0]
                    new_col = col + i[1]
                    if 0 <= new_row < n and 0 <= new_col < n:
                        if visit[new_row][new_col][2] == False:
                            visit[new_row][new_col][2] = True
                            queue.append([new_row, new_col, 2])

        for i in range(3):
            if visit[dic[want][0]][dic[want][1]][i] == True:
                queue_temp.append([dic[want][0], dic[want][1], i])
                visit_temp[dic[want][0]][dic[want][1]][i] = True

        if len(queue_temp) != 0:
            queue = queue_temp
            visit = visit_temp
            want = want + 1

        print("result :",result)
        for i in visit:
            print(i)
        print("----------------------")


bfs()
print(result)
