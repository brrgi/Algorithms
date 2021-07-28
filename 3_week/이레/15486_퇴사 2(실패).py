import sys
input=sys.stdin.readline
n=int(input())
t=[]
p=[]
dp=[0 for i in range(n)]


def init(day):
    for i in range(day):
        ipt = list(map(int, input().split()))
        t.append(ipt[0])
        p.append(ipt[1])
    if t[i]<=n:
        dp[0]=p[0]

init(n)

for i in range(1, n):
    if i+t[i]>n:
        continue
    for j in range(i):
        if (i-j)>=(t[j]):
            dp[i]=max(dp[i], dp[j]+p[i])
print(max(dp))