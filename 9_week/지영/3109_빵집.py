BLOCK = 'x'

N, M = map(int, input().split())
maps = [input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# ↗ ↘ → 
moveable = [[-1, 1], [0, 1], [1, 1]]

ret = 0
def dfs(row, col):
    
    for elm in moveable:
        r = row + elm[0]
        c = col + elm[1]
        
        if r < 0 or r > N-1 or c < 0 or c > M-1: continue
        
        if visited[r][c]: continue

        # 이미 가고자하는 간선의 대각선 방향으로 간 이력이 있는지 검사
        if row - 1 > 0 and r + 1 < N and visited[row-1][c] and visited[r+1][c]: continue
        if r - 1 > 0 and row + 1 < N and visited[row+1][c] and visited[r-1][c]: continue

        # 끝에 도달한 경우, return 1
        if c == M-1: return 1


        if maps[r][c] == BLOCK: continue

        visited[r][c] = True

        if dfs(r, c): return 1
    
    return 0

for start in range(N):
    ret += dfs(start, 0)

print(ret)