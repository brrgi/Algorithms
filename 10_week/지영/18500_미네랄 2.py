from collections import deque
N, M = map(int, input().split())
cave_maps = [list(input()) for _ in range(N)]

exec = int(input())
heights = list(map(int, input().split()))

EVEN = 0
ODD = 1
MINERAL = 'x'
EMPTY = '.'

moveable = [[[-1, 0], [0, 1], [1, 0]], [[-1, 0], [0, -1], [1, 0]]]

def remove_mineral(num: int):
    pos = N - heights[num]

    if num % 2 == EVEN:
        # 오른쪽에서 왼쪽 
        for col in range(M):
            if cave_maps[pos][col] == MINERAL:
                return [pos, col]
    else:
        # 왼쪽에서 오른쪽
        for col in range(M-1, -1, -1):
            if cave_maps[pos][col] == MINERAL:
                return [pos, col]
    return None
    
def is_reachable(removed:list, st):

    for r, c  in moveable[st]:

        row = removed[0] + r
        col = removed[1] + c

        if col < 0 or col > M-1 or row < 0 or row > N-1: continue
        if cave_maps[row][col] == EMPTY: continue

        visited = [[False] * M for _ in range(N)]
        visited[row][col] = True
        cluster = set()
        cluster.add((row, col))

        reachable = False
        queue = deque([[row, col]])

        while queue:

            pop = queue.popleft()

            for r2, c2  in [[1, 0], [0, 1], [-1, 0], [0, -1]]:

                moved_r = pop[0] + r2
                moved_c = pop[1] + c2

                if moved_c < 0 or moved_c > M-1 or moved_r < 0 or moved_r > N-1: continue

                if cave_maps[moved_r][moved_c] == EMPTY: continue
                if visited[moved_r][moved_c]: continue
                
                # 해당 클러스터가 바닥이랑 연결된 상태이므로 움직일 필요가 없는 클러스터임
                if moved_r == N-1: 
                    reachable = True 
                    break


                queue.append([moved_r, moved_c])
                visited[moved_r][moved_c] = True
                cluster.add((moved_r, moved_c))
        
        if not reachable:
            move_cluster(cluster)
            break
    

def move_cluster(cluster: set):
    
    flag = False
    cnt = 0
    already =  [[False] * M for _ in range(N)]
    
    while not flag:
        cnt += 1

        for row, col in cluster:

            if row + cnt == N-1:
                flag = True
                break

            if cave_maps[row+cnt+1][col] == MINERAL: 
                if (row+cnt+1, col) not in cluster:
                    flag = True
                    break
    
    for row, col in cluster:
        if not already[row][col]:
            cave_maps[row][col] = EMPTY
        
        cave_maps[row + cnt][col] = MINERAL
        already[row + cnt][col] = True

def solution():

    for num in range(exec):
        removed = remove_mineral(num)
        if not removed: continue

        cave_maps[removed[0]][removed[1]] = EMPTY

        # 현재 삭제된 미네랄 그 주변에 붙어있는 모든 클러스터 조사
        is_reachable(removed, num % 2)
    

    for map in cave_maps:
        print(''.join(map))

solution()
