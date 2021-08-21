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
bishop_default=[(1,1),(1,-1),(-1,1),(-1,-1)]
bishop=[]
result = 0

dic=dict()

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(len(t)):
        if t[j] == 1:
            start = [i, j]
        dic[t[j]]=[i,j]
    maps.append(t)

for i in range(1,n):
    for j in bishop_default:
        bishop.append((j[0]*i,j[1]*i))
def bfs():
    global result
    queue = deque()
    queue.append(start)
    visit = [[False] * n for _ in range(n)]
    visit[start[0]][start[1]] = True
    want=start[2]+1
    while queue and want!=10 and result<100:
        cnt = len(queue)
        result += 1
        # print(want, result)
        for _ in range(cnt):
            row, col = queue.popleft()

            #step 1 : 나이트 움직이기
            for i in knight:
                new_row = row + i[0]
                new_col = col + i[1]
                if 0 <= new_row < n and 0 <= new_col < n:
                    if visit[new_row][new_col] == False:
                        visit[new_row][new_col] = True
                        queue.append([new_row, new_col])

            #step 2 : 룩 움직이기
            for i in range(n):
                if visit[row][i]==False:
                    visit[row][i]=True
                    queue.append([row, i])
                if visit[i][col]==False:
                    visit[i][col]=True
                    queue.append([i, col])

            #step 3 : 비숍 움직이기
            for i in bishop:
                new_row = row + i[0]
                new_col = col + i[1]
                if 0 <= new_row < n and 0 <= new_col < n:
                    if visit[new_row][new_col] == False:
                        visit[new_row][new_col] = True
                        queue.append([new_row, new_col])

            if visit[dic[want][0]][dic[want][1]]==True:
                queue=deque()
                queue.append((dic[want][0],dic[want][1]))
                visit = [[False] * n for _ in range(n)]
                visit[dic[want][0]][dic[want][1]]=True
                want=want+1
                break

            # for i in visit:
            #     print(i)
            # return
bfs()
print(result)