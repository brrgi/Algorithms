'''
    1. 기관차는 항상 3대
    2. 기관차가 끌고갈 수 있는 객차 수 maximum
'''
n = int(input())
trains = list(map(int, input().split()))
maximum = int(input())
sums = []
start = 0
for t in trains:
    start += t
    sums.append(start)
sums = [0] + sums
dp = [[0] * (50001) for _ in range(4)]      #dp[4][50001]

for i in range(1, 4):
    for m in range(i * maximum, n + 1):
        if i == 1:
            dp[i][m] = max(sums[m] - sums[m - maximum], dp[i][m - 1])
        else:
            dp[i][m] = max(dp[i - 1][m - maximum] + sums[m] - sums[m - maximum], dp[i][m - 1])

print(dp[3][n])



import sys

input = sys.stdin.readline
N = int(input())
train = list(map(int, input().split()))
limit = int(input())


input = sys.stdin.readline
N = int(input())
train = list(map(int, input().split()))
limit = int(input())
S = [0]
value = 0
for t in train:
    value += t
    S.append(value)
dp = [[0] * (N + 1) for _ in range(4)]
for n in range(1, 4):
    for m in range(n * limit, N + 1):
        if n == 1:
            dp[n][m] = max(dp[n][m - 1], S[m] - S[m - limit])
        else:
            dp[n][m] = max(dp[n][m - 1], dp[n - 1][m - limit] + S[m] - S[m - limit])
print(dp[3][N])
