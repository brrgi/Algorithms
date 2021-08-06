N = int(input()) #7
scheduled = [list(map(int, input().split()))for _ in range(N)] #time, period
# 현재 날짜 기준 최대값 저장
max_val = [0 for _ in range(N+1)]
ret = 0
for idx, elm in reversed(list(enumerate(scheduled))):
    if idx + elm[0] > N: 
        max_val[idx] = ret
        continue
    max_val[idx] = max(ret, max_val[idx + elm[0]] + elm[1])
    ret = max_val[idx]

print(ret)


