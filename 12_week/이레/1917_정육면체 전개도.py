def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

#정육면체 전개도가 되는 방법은 11가지
for i in range(3):
    check=0
    for j in range(6):
        t=list(map(int, input().split()))
        if t.count(0)==0:
            check+=1
        print(t, check)
    break