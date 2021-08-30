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
dp = [[0] * (50001) for _ in range(4)]

for i in range(1, 4):
    for m in range(i * maximum, n + 1):
        if i == 1:
            dp[i][m] = max(sums[m] - sums[m - maximum], dp[i][m - 1])
        else:
            dp[i][m] = max(dp[i - 1][m - maximum] + sums[m] - sums[m - maximum], dp[i][m - 1])

print(dp[3][n])
