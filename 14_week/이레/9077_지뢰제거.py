t=int(input())
mine=[[] for _ in range(t)]
for i in range(t):
    n=int(input())
    for j in range(n):
        x,y=map(int, input().split())
        mine[i].append([x,y])

for i in mine:
    print(i)