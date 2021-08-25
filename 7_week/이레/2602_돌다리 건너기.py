'''
    R I N G S -> 5개의 문자로 이루어진 다리
'''
import sys
input=sys.stdin.readline
magic = input().rstrip()
devil = input().rstrip()
angel = input().rstrip()
magic_length = len(magic)
stone_length = len(devil)
dp = [[[0, 0] for _ in range(101)] for _ in range(21)]  # 두루마리 문자열 길이 20, 돌다리 100, 위아래 2개 [21][101][2]

# init dp setting -
for i in range(stone_length + 1):
    dp[0][i][0] = 1
    dp[0][i][1] = 1
 # magic 두루마리 문자열 길이 20, 돌다리 100, 위아래 2개 [21][101][2]

 #RGS 1-3
for i in range(1, magic_length+1):      #마법 두루마리 길이
    for j in range(1, stone_length+1):  #돌다리 길이
        if magic[i - 1] == angel[j - 1]:
            dp[i][j][0] += dp[i - 1][j - 1][1]
        if magic[i - 1] == devil[j - 1]:
            dp[i][j][1] += dp[i - 1][j - 1][0]
        dp[i][j][0] += dp[i][j - 1][0]
        dp[i][j][1] += dp[i][j - 1][1]

print(sum(dp[magic_length][stone_length]))