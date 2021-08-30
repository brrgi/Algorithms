
from collections import deque
N = int(input())

queue = deque()
matrix = [[] for _ in range(N)]
visited = [[[[False]*(N**2+2) for _ in range(3)] for _ in range(N)] for _ in range(N)]

global start

for row in range(N):
    for col, val in enumerate(map(int, input().split())):
        if val == 1:
            start = [row, col]
        matrix[row].append(val)

for obj in range(3):    
    queue.append([start[0], start[1], obj, 2, 0])
    visited[start[0]][start[1]][obj][2] = True
store = {}

while queue:
    row, col, object, dest, time = queue.popleft()
    if dest not in store:
        if dest == 18: 
            print(time)
        store[dest] = time
    else:
        store[dest] = min(store[dest], time)

    if dest == N**2 + 1:
        print(time)
        print(store)
        break

    # 기물 체인지
    for obj in range(3):
        if object == obj: continue

        if visited[row][col][object][dest]: continue

        queue.append([row, col, obj, dest, time+1]) 
        visited[row][col][obj][dest] = True


    # 룩
    if object == 0:
        for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            for offset in range(1, N):
                moveble_row = row + r * offset
                moveable_col = col + c * offset
                if moveble_row < 0 or moveable_col < 0 or moveble_row > N-1 or moveable_col > N-1 : break
                
                if visited[moveble_row][moveable_col][object][dest]: continue
                visited[moveble_row][moveable_col][object][dest] = True

                if matrix[moveble_row][moveable_col] == dest:
                    queue.append([moveble_row, moveable_col, object, dest+1, time+1])
                    
                else:
                    queue.append([moveble_row, moveable_col, object, dest, time+1])
    # 비숍
    elif object == 1:

        for r, c in [[-1,-1], [-1, 1], [1, 1], [1, -1]]:
            for offset in range(1, N):
                moveble_row = row + r * offset
                moveable_col = col + c * offset
                if moveble_row < 0 or moveable_col < 0 or moveble_row > N-1 or moveable_col > N-1 : break
                

                if visited[moveble_row][moveable_col][object][dest]: continue
                visited[moveble_row][moveable_col][object][dest] = True

                if matrix[moveble_row][moveable_col] == dest:
                    queue.append([moveble_row, moveable_col, object, dest+1, time+1])

                else:
                    queue.append([moveble_row, moveable_col, object, dest, time+1])


    elif object == 2:

        for r, c in [[-1, 2], [2, -1], [1, 2], [2, 1], [-2, 1], [1, -2], [-2, -1], [-1, -2]]:
            moveble_row = row + r
            moveable_col = col + c

            if moveble_row < 0 or moveable_col < 0 or moveble_row > N-1 or moveable_col > N-1 : continue

            if visited[moveble_row][moveable_col][object][dest]: continue
            visited[moveble_row][moveable_col][object][dest] = True

            if matrix[moveble_row][moveable_col] == dest:
                queue.append([moveble_row, moveable_col, object, dest+1, time+1])
            else:
                queue.append([moveble_row, moveable_col, object, dest, time+1])


# 5
# 18 21 24 13 3
# 10 19 22 11 15
# 6 2 14 25 8
# 7 23 9 1 17
# 20 12 5 16 4


# {2=0, 3=1, 4=4, 5=5, 6=6, 7=8, 8=9, 9=11, 10=13, 11=15, 12=16, 13=18, 14=20, 15=22, 16=23, 17=25, 18=27, 19=30, 20=31, 21=33, 22=36, 23=38, 24=39, 25=41, 26=42}


# {2: 0, 3: 1, 4: 4, 5: 5, 6: 6, 7: 8, 8: 9, 9: 11, 10: 13, 11: 15, 12: 16, 13: 18, 14: 20, 15: 22, 16: 23, 17: 25, 18: 27, 19: 30, 20: 32, 21: 34, 22: 36, 23: 38, 24: 40, 25: 42, 26: 43}