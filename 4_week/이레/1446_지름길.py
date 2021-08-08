import sys

input = sys.stdin.readline
n, d = map(int, input().split())
inp = []
dp = [i for i in range(d + 1)]
for i in range(n):
    t = list(map(int, input().split()))
    if t[1] <= d:
        inp.append(t)

for i in range(d + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    for j in inp:
        if i == j[0]:
            dp[j[1]] = min(dp[j[1]], dp[j[0]] + j[2])


print(dp[-1])
