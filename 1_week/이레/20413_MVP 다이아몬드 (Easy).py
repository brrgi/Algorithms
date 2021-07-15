m=int(input())
s,g,p,d=map(int, input().split())
mvp=input()
result=[0 for i in range(len(mvp))]

start=0
if mvp[0]=='B':
    start=s-1
elif mvp[0]=='S':
    start=g-1
elif mvp[0]=='G':
    start=p-1
elif mvp[0]=='P':
    start=d-1
else:
    start=d
result[0]=start

for i in range(m-1):
    if mvp[i+1] == 'B':
        result[i+1]=(s-1)-result[i]
    elif mvp[i+1] == 'S':
        result[i + 1] = (g - 1) - result[i]
    elif mvp[i+1] == 'G':
        result[i + 1] = (p - 1) - result[i]
    elif mvp[i+1] == 'P':
        result[i + 1] = (d - 1) - result[i]
    else:
        result[i+1]=d

# print(result)
print(sum(result))
