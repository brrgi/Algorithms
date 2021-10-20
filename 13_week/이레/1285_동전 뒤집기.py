import sys

input = sys.stdin.readline
n = int(input())
coins = []
result = n * n

for i in range(n):
    coins.append(list(input()))


def reverse(ch):
    if ch == 'H':   return 'T'
    return 'H'

for i in range(1 << n): #2의 n승번 0~2^n
    all = 0
    for j in range(n):      #세로
        t = 0
        for q in range(n):  #가로
            now = coins[q][j]
            if (i & (1 << q)) != 0:   now = reverse(now)    #뒤집기
            if now == 'T':    t += 1
        all += min(n - t, t)
    result = min(result, all)
print(result)
