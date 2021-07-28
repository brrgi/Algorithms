import sys

input = sys.stdin.readline
n = int(input())
t = []
p = []
dp = [0 for _ in range(n + 1)]


def init(day):
    for i in range(day):
        ipt = list(map(int, input().split()))
        t.append(ipt[0])
        p.append(ipt[1])


init(n)
start = 0

for i in range(n):
    start = max(start, dp[i])
    print(start, dp)
    if i + t[i] > n:        #n일을 넘어버리는 경우
        continue
    dp[i + t[i]] = max(dp[i + t[i]], start + p[i])      #현재가 아닌 t[i]일 후의 dp를 갱신

print(max(dp))
