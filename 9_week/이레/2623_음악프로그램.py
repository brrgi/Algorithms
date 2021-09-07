n,m=map(int, input().split())
come=[0 for i in range(n)]
go=[[] for i in range(n)]
result=[]
for i in range(m):
    t=list(map(int, input().split()))
    for j in range(1, len(t)-1):
        go[t[j]-1].append(t[j+1])
        come[t[j+1]-1]+=1

checks=[0 for i in range(n)]
while 1:
    check=0
    visit=[0 for i in range(n)]
    for i in range(n):
        if come[i]==0 and checks[i]==0:
            check+=1
            visit[i]=1
            checks[i]=1
            result.append(i+1)
    for i in range(n):
        if visit[i]==1:
            for j in go[i]:
                come[j-1]-=1
            go[i]=[]

    if check==0:
        break
if len(result)!=n:
    print(0)
    exit()
for i in result:
    print(i)