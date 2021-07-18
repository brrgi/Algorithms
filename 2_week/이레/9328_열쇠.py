import sys
from collections import deque

input=sys.stdin.readline
lower_case=set()
upper_case=set()
dir=[(0,1),(0,-1),(1,0),(-1,0)]
for i in range(26):
    lower_case.add(chr(97+i))
    upper_case.add(chr(65+i))

t=int(input())
for i in range(t):
    h,w=map(int,input().split())
    keys=set()
    maps=[]
    queue = deque()
    result=0
    visit=[[False for _ in range(w)] for _ in range(h)]
    temp=[]
    # print(i+1,"번 시작")
    for i in range(h):
        line=list(input().strip())
        maps.append(line)

    for i in input().strip():
        if i=='0':
            break
        keys.add(i)

    for i in range(h):
        for j in range(w):
            if i==0 or i==h-1:
                if maps[i][j] == '$':
                    queue.append((i, j))
                    result+=1
                    visit[i][j] = True
                elif maps[i][j]=='.':
                    queue.append((i,j))
                    visit[i][j] = True
                elif maps[i][j]!='*':
                    if maps[i][j] in lower_case:
                        queue.append((i,j))
                        visit[i][j] = True
                    else:
                        if maps[i][j].lower() in keys:
                            queue.append((i,j))
                            visit[i][j] = True
                        else:
                            temp.append((i,j))
            else:
                if j==0 or j==w-1:
                    if maps[i][j] == '$':
                        queue.append((i, j))
                        result += 1
                        visit[i][j] = True
                    elif maps[i][j] == '.':
                        queue.append((i, j))
                        visit[i][j] = True
                    elif maps[i][j] != '*':
                        if maps[i][j] in lower_case:
                            queue.append((i, j))
                            visit[i][j] = True
                        else:
                            if maps[i][j].lower() in keys:
                                queue.append((i, j))
                                visit[i][j] = True
                            else:
                                temp.append((i, j))

    while queue:
        # print(queue)
        length=len(queue)
        for i in range(length):
            data=queue.popleft()
            row=data[0]
            col=data[1]


            for d in dir:
                new_row=row+d[0]
                new_col=col+d[1]
                if 0<=new_row<h and 0<=new_col<w and visit[new_row][new_col]==False:
                    if maps[new_row][new_col]=='*':
                        continue
                    if maps[new_row][new_col] == '$':
                        # print("옴???")
                        queue.append((new_row,new_col))
                        result += 1
                        visit[new_row][new_col] = True
                    elif maps[new_row][new_col]=='.':
                        queue.append((new_row,new_col))
                        visit[new_row][new_col]=True
                    elif maps[new_row][new_col] in lower_case:  #소문자인 경우
                        queue.append((new_row,new_col))
                        keys.add(maps[new_row][new_col])
                        visit[new_row][new_col]=True
                    else:                                       #대문자인 경우
                        if maps[new_row][new_col].lower() in keys:
                            queue.append((new_row,new_col))
                            visit[new_row][new_col]=True
                        else:
                            temp.append((new_row,new_col))
        for t in temp:
            if maps[t[0]][t[1]].lower() in keys:
                if visit[t[0]][t[1]]==False:
                    visit[t[0]][t[1]]=True
                    # print("확인용", t[0], t[1])
                    queue.append((t[0],t[1]))

    print(result)