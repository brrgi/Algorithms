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


for i in range(1 << n):
    all = 0
    for j in range(n):
        t = 0
        for q in range(n):
            now = coins[q][j]
            if (i & (1 << q)) != 0:   now = reverse(now)
            if now == 'T':    t += 1
        all += min(n - t, t)
    result = min(result, all)
print(result)
