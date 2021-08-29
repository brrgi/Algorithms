#1시 59분 -> 2시 16분(17분)
from collections import deque
#p:응시자 o:지나감 x:벽
def solution(places):
    answer = []
    dir=[(1,0),(-1,0),(0,1),(0,-1)]
    for place in places:
        rule=1
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P':
                    queue=deque()
                    visit=[[0 for _ in range(5)] for _ in range(5)]
                    queue.append([i,j])
                    visit[i][j]=1
                    for i in range(2):
                        if len(queue)==0:
                            break
                        leng=len(queue)
                        for i in range(leng):
                            data=queue.popleft()
                            for r,c in dir:
                                new_r=data[0]+r
                                new_c=data[1]+c
                                if 0<=new_r<5 and 0<=new_c<5:
                                    if place[new_r][new_c]!='X' and visit[new_r][new_c]==0:
                                        if place[new_r][new_c] == 'P':
                                            rule = 0
                                        print(new_r, new_c)
                                        visit[new_r][new_c]=1
                                        queue.append([new_r, new_c])
        answer.append(rule)
    return answer



places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)
