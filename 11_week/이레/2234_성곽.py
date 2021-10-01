dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 1=서 2=북 4=동 8=남
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
visit = [[0 for _ in range(n)] for _ in range(m)]
first = 0
second = 0
max_value = -1
nums=[]

def dfs(row, col, val):
    global nums
    visit[row][col] = val
    nums[val-1]+=1
    number = maps[row][col]
    if number & 1 == 0:
        next_row, next_col = row + dir[0][0], col + dir[0][1]
        if 0 <= next_row < m and 0 <= next_col < n and visit[next_row][next_col] == 0:
            dfs(next_row, next_col, val)
    if number & 2 == 0:
        next_row, next_col = row + dir[1][0], col + dir[1][1]
        if 0 <= next_row < m and 0 <= next_col < n and visit[next_row][next_col] == 0:
            dfs(next_row, next_col, val)
    if number & 4 == 0:
        next_row, next_col = row + dir[2][0], col + dir[2][1]
        if 0 <= next_row < m and 0 <= next_col < n and visit[next_row][next_col] == 0:
            dfs(next_row, next_col, val)
    if number & 8 == 0:
        next_row, next_col = row + dir[3][0], col + dir[3][1]
        if 0 <= next_row < m and 0 <= next_col < n and visit[next_row][next_col] == 0:
            dfs(next_row, next_col, val)


res = 0
for i in range(m):
    for j in range(n):
        if visit[i][j] == 0:
            res += 1
            nums.append(0)
            dfs(i, j, res)

for i in range(m):
    for j in range(n):
        for r,c in dir:
            if 0<=i+r<m and 0<=j+c<n:
                if visit[i][j]!=visit[i+r][j+c]:
                    max_value=max(nums[visit[i][j]-1]+nums[visit[i+r][j+c]-1], max_value)


print(len(nums))
print(max(nums))
print(max_value)