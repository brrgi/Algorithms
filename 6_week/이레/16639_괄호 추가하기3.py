import sys

n = int(input())
strs = input().rstrip()
leng = n // 2 + 1
op = []
"""
    n<19 이므로 숫자는 최대 10개
    dp[2][i][j] j->i->2(큰 값 작은 값) 은 mix min 비교가 안되므로 따로 나눌 것
    -> max_dp[i][j]
    -> min_dp[i][j]
    max = sys.maxsize,  min = -sys.maxsize - 1.
"""
max_dp = [[-sys.maxsize - 1 for _ in range(10)] for _ in range(10)]
min_dp = [[sys.maxsize for _ in range(10)] for _ in range(10)]

for i in range(leng):
    max_dp[i][i] = min_dp[i][i] = int(strs[2 * i])
for i in range(leng - 1):
    op.append(strs[2 * i + 1])

def cal(a,b,operation):
    if operation=='+':
        return a+b
    elif operation=='-':
        return a-b
    elif operation=='*':
        return a*b

for q in range(leng - 1):  # ex leng = 0 1 2 3
    for i in range(leng - (q + 1)):
        print("구간", i, "~", q + 1 + i)
        val=[]
        val.append(cal(min_dp[i][i], min_dp[i+1][q+i+1], op[i]))
        val.append(cal(max_dp[i][i], min_dp[i+1][q+i+1], op[i]))
        val.append(cal(min_dp[i][i], min_dp[i+1][q+i+1], op[i]))
        val.append(cal(man_dp[i][i], min_dp[i+1][q+i+1], op[i]))
    print()
