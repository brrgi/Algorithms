from collections import deque

PERSON = 'P'
EMPTY = 'O'
PARTITION = 'X'
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col, place):
    queue = deque()
    queue.append([row, col])

    visited = [[False] * 5 for _ in range(5)]
    visited[row][col] = True

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):
            next_row = cur_row + dr[i]
            next_col = cur_col + dc[i]

            if next_row < 0 or next_col < 0 or next_row > 4 or next_col > 4: continue
            if visited[next_row][next_col]: continue

            dist = abs(next_row - row) + abs(next_col - col)

            if dist > 2: continue

            if place[next_row][next_col] == EMPTY:
                queue.append([next_row, next_col])
                visited[next_row][next_col] = True
                continue
            
            cnt = 0
            if place[next_row][next_col] == PERSON:
                if abs == 1: 
                    return False
                
                for j in range(4):
                    temp_row = next_row + dr[i]
                    temp_col = next_col + dc[i]

                    if temp_row < 0 or temp_col < 0 or temp_row > 4 or temp_col > 4: continue
                    if abs(temp_row - row) + abs(temp_col - col) != 1: continue


                    if abs(temp_row - row) + abs(temp_col - col) == 1 and place[temp_row][temp_col] == PARTITION:
                        cnt += 1

                if next_row == row or next_col == col:
                    if cnt != 1: 
                        return False
                else:
                    if cnt != 2: 
                        return False
    
    return True

def search_row(idx, row, place):

    for idx2, elm in enumerate(row):

        if elm == PERSON:
            ret = dfs(idx, idx2, place)

            if not ret: return False
        
    return True


def solution(places):

    answer = []

    for place in places:
        flag = True


        for idx, row in enumerate(place):
            ret = search_row(idx, row, place)

            if not ret: 
                flag = False
                break
            
        if not flag: 
            answer.append(0)
            continue

        answer.append(1)

    return answer


        

# N = int(input())
# p = [[input() for _ in range(5) ] for _ in range(N)]
p = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# p = [["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]]
print(solution(p))








