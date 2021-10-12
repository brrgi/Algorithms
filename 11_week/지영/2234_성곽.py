from collections import deque
N, M = map(int, input().split())

"""
    모든 row, col을 조회하며, 방문한적이 없는 칸을 bfs로 조회하여 전체 클러스터를 조회한다.
    이때, 각각의 클러스터의 소속을 visited 배열 안에 저장해 두는 것이 매우 중요하다.

    단순히 몇개의 성광이 있는지, 각각의 성곽의 사이즈가 몇이진, 어떤 성곽의 사이즈가 최대인지는 각각의 row, col을 조회하면서 
    해결할 수 있지만, 어떤 성곽이 연결되어있고, 이를 연결 시킬 수 있는지 여부, 또 연결시켰을때 각 성곽의 크기가 얼마가 되여야 하는지에 여부는
    visited 배열을 어떻게 초기화 해놓는지에 따라 N2로 해결할 수 있다.

    1 1 2 2 3 
    1 2 2 2 3

    던순 위와 같이 visited 배열이 구성되었다면, 1, 2가 각 노드로부터 상하 좌우를 조회하면 본인과 다른 클러스터를 가진 값이 있다면 
    각각의 클러스터의 사이즈를 더한 값을 최대값과 비교해 업데이트 해주면 된다. 

    해결: bfs + 비트 마스킹 + visited 배열의 초기화

"""


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


#  서, 북, 동, 남 = 1, 2, 4, 8
maps = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N  for _ in range(M)]
cluster = {}


total = 0
max_size = 0

def bfs(row, col):

    queue = deque()
    queue.append([row, col])
    visited[row][col] = total
    size = 1

    while queue:
        row, col = queue.popleft()

        for dir in range(4):
            n_row = row + dr[dir]
            n_col = col + dc[dir]

            if n_row < 0 or n_row > M-1 or n_col < 0 or n_col > N-1: continue
            if visited[n_row][n_col]: continue
            if maps[n_row][n_col] & (1 << dir): continue

            queue.append([n_row, n_col])
            visited[n_row][n_col] = total
            size += 1

    cluster[total] = size
    return size

for row in range(M):
    for col in range(N):
        if visited[row][col]: continue
        total += 1
        max_size = max(max_size, bfs(row, col))
        
ret = 0

for row in range(M-1):
    for col in range(N-1):
        if visited[row][col] != visited[row][col +1]:
            ret = max(ret, cluster[visited[row][col]] + cluster[visited[row][col +1]])

        if visited[row][col] != visited[row+1][col]:
            ret = max(ret, cluster[visited[row][col]] + cluster[visited[row+1][col]])


print(total)
print(max_size)
print(ret)