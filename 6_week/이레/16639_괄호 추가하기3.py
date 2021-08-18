"""
    n<19 이므로 숫자는 최대 10개
    dp[2][i][j] j->i->2(큰 값 작은 값) 은 mix min 비교가 안되므로 따로 나눌 것
    -> max_dp[i][j]
    -> min_dp[i][j]
    max = sys.maxsize,  min = -sys.maxsize - 1.
"""
import sys

n = int(input())
strs = input().rstrip()
leng = n // 2 + 1
max_dp = [[-sys.maxsize - 1 for _ in range(n)] for _ in range(n)]
min_dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for i in range(n):
    if i%2==0:
        max_dp[i][i] = min_dp[i][i] = int(strs[i])

def cal(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b

#https://ltk3934.tistory.com/24
for j in range(2, n, 2):
    for i in range(0, n - j, 2):
        for k in range(2, j + 1, 2):
            val = []
            val.append(cal(max_dp[i][i + k - 2], max_dp[i + k][i + j], strs[i + k - 1]))
            val.append(cal(max_dp[i][i + k - 2], min_dp[i + k][i + j], strs[i + k - 1]))
            val.append(cal(min_dp[i][i + k - 2], max_dp[i + k][i + j], strs[i + k - 1]))
            val.append(cal(min_dp[i][i + k - 2], min_dp[i + k][i + j], strs[i + k - 1]))
            val.sort()

            min_dp[i][i + j] = min(min_dp[i][i + j], val[0])
            max_dp[i][i + j] = max(max_dp[i][i + j], val[3])

print(max_dp[0][n - 1])
