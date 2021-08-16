'''
    S 개의 곡
    세 사람 중 한 명이 불러야 한다. (여러 명이 불러도 된다.)
    d만, k만, h만, d k, d h, k h, d k h
    s는 최대 50
'''
s,d,k,h=map(int, input().split())
dp = [[[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

"""
    가지치기
    - 전부 다 불렀을 때
        - 3명이 불러야 하는 만큼 다 부름    ->  1
        - 다 못부름 ->  0
    - 3명 중 불러야 하는 만큼보다 더 불렀을 때  ->  1
    - 이미 방문한 경우 -> dp[s][d][k][h]
"""


def dfs(s, d, k, h):
    if s==0:
        if d == 0 and k == 0 and h == 0:
            return 1
        return 0

    if d<0 or k<0 or h<0:
        return 0

    if dp[s][d][k][h]!=-1:
        return dp[s][d][k][h]

    dp[s][d][k][h]=0

    dp[s][d][k][h]+=dfs(s-1,d-1,k,h)
    dp[s][d][k][h]+=dfs(s-1,d,k-1,h)
    dp[s][d][k][h]+=dfs(s-1,d,k,h-1)
    dp[s][d][k][h]+=dfs(s-1,d-1,k-1,h)
    dp[s][d][k][h]+=dfs(s-1,d-1,k,h-1)
    dp[s][d][k][h]+=dfs(s-1,d,k-1,h-1)
    dp[s][d][k][h]+=dfs(s-1,d-1,k-1,h-1)

    dp[s][d][k][h]%=1000000007

    return dp[s][d][k][h]

print(dfs(s,d,k,h))