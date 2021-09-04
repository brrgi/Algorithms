r, c = map(int, input().split())
dir = [(-1, 1), (0, 1), (1, 1)]  # 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선
maps = [list(input()) for _ in range(r)]
visit = [[0 for _ in range(c)] for _ in range(r)]
result = 0


def dfs(row, col):
    global result
    if col == c - 1:
        result += 1
        return 1

    for d in dir:
        new_row = row + d[0]
        new_col = col + d[1]
        if 0 <= new_row < r and 0 <= new_col < c:
            if maps[new_row][new_col] == '.':
                if visit[new_row][new_col] == 0:
                    visit[new_row][new_col] = 1
                    go = dfs(new_row, new_col)
                    if go == 1:
                        return 1
    return 0


for i in range(r):
    visit[i][0] = 1
    dfs(i, 0)

print(result)
