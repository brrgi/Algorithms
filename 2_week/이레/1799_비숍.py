n=int(input())
chess=[]
result1=[]
result2=[]
left=[0 for _ in range(20)]
right=[0 for _ in range(20)]

for i in range(n):
    chess.append(list(map(int,input().split())))
# print(chess)

def dfs(row, col, cnt, color):
    if col>=n:
        row+=1
        if col%2==0:
            col=1
        else:
            col=0

    if row>=n:
        if color==1:
            result1.append(cnt)
        else:
            result2.append(cnt)
        return

    if chess[row][col]==1 and left[col - row + n - 1]==0 and right[row + col]==0:
        left[col - row + n - 1] = right[row + col] = 1
        dfs(row, col + 2, cnt + 1, color)
        left[col - row + n - 1] = right[row + col] = 0
    dfs(row, col+2, cnt, color)

dfs(0,0,0,0)
dfs(0,1,0,1)

print(max(result1)+max(result2))