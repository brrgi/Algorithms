import sys
input=sys.stdin.readline
m,n=map(int ,input().split())   #가로세로크기 m, 날짜 수 n
maps=[1 for i in range(2*m-1)]

def select_max_value(row, col):
    return max(maps[row-1][col],maps[row-1][col-1],maps[row][col-1])

for i in range(n):
    zero, one, two=map(int,input().split())

    #rule 1
    for j in range(zero, zero+one):
        maps[j]+=1
    for j in range(zero+one,2*m-1):
        maps[j]+=2



for i in range(m):
    print(maps[m-1-i],end=' ')
    for j in range(m,2*m-1):
        print(maps[j], end=' ')
    print()