from collections import deque
dir=[[0,1],[0,-1],[-1,0],[1,0]]   #→, ←, ↑, ↓

#들어온 화살표를 반대 방향으로 돌린다.
#매개변수 : index의 값을 넘긴다.
def reverse_direction(number):
    if number==0:
        return 1
    if number == 1:
        return 0
    if number == 2:
        return 3
    if number == 3:
        return 2

n,k=map(int, input().split())   #체스판 크기, 말의 개수
maps=[[2 for _ in range(n+2)] for _ in range(n+2)]
for i in range(1,n+1):
    t=list(map(int, input().split()))
    for j in range(1,n+1):
        maps[i][j]=t[j-1]

visit=[[[] for _ in range(n+2)] for _ in range(n+2)]

queue=deque()
for i in range(k):
    row, col, arrow=map(int, input().split())
    arrow-=1
    queue.append([row, col])
    visit[row][col].append(arrow)

for i in visit:
    print(i)
print("-------------------------")
start=0
while queue:
    start+=1
    leng=len(queue)

    if start>1000:
        print(-1)
        break
    if leng==1:
        print(start-1)
        break
    print("턴 ", start)
    for i in range(leng):
        r,c=queue.popleft()
        a=visit[r][c][0]        #현재 가리키는 방향
        next_row=r+dir[a][0]
        next_col=c+dir[a][1]
        if maps[next_row][next_col]==0:   #다음 곳이 흰색일 때
            if visit[next_row][next_col]==[]:
                queue.append([next_row, next_col])
            visit[next_row][next_col] += visit[r][c]
            visit[r][c] = []
        elif maps[next_row][next_col]==1: #빨간색
            if visit[next_row][next_col]==[]:
                queue.append([next_row, next_col])
            visit[next_row][next_col] += reversed(visit[r][c])
            visit[r][c] = []
        else:                                   #파란색
            a=reverse_direction(a)
            visit[r][c][0]=a
            next_row = r + dir[a][0]
            next_col = c + dir[a][1]
            if maps[next_row][next_col] == 0:  # 다음 곳이 흰색일 때
                if visit[next_row][next_col] == []:
                    queue.append([next_row, next_col])
                visit[next_row][next_col] += visit[r][c]
                visit[r][c] = []
            elif maps[next_row][next_col] == 1:  # 빨간색
                if visit[next_row][next_col] == []:
                    queue.append([next_row, next_col])
                visit[next_row][next_col] += reversed(visit[r][c])
                visit[r][c] = []
            else:
                queue.append([r, c])
        #
        # for i in visit:
        #     print(i)
        # print("000000000000000000000000000")