from collections import deque
dir=[[0,1],[0,-1],[-1,0],[1,0]]
r,c=map(int, input().split())
maps=[list(input()) for _ in range(r)]
n=int(input())
rods=list(map(int, input().split()))
queue=deque()

def make_queue(row, col):
    for r,c in dir:
        queue.append([row+r, col+c])


for i, rod in enumerate(rods):
    floor=r-rod
    if i%2==0:  #왼쪽
        for j in range(c):
            if maps[floor][j]=='x':
                maps[floor][j]='.'
                make_queue(floor,j)
                break
    else:       #오른쪽
        ch=0
        for j in range(c):
            if maps[floor][j] == 'x':
                ch=j
        make_queue(floor, ch)
        maps[floor][ch]='.'

