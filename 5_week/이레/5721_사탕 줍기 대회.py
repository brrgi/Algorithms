while 1:
    m, n = map(int, input().split())
    if m == n and m == 0:
        break
    maps = []
    for i in range(m):
        maps.append(list(map(int, input().split())))

    row_max = [0 for i in range(m)]
    for i in range(m):
        dp = [0 for _ in range(n)]
        dp[0] = maps[i][0]

        for j in range(1, n):
            if j == 1:
                dp[j] = max(dp[j - 1], maps[i][j])
                continue
            dp[j] = max(dp[j - 1], dp[j - 2] + maps[i][j])
        row_max[i] = dp[-1]

    result = [0 for _ in range(m)]
    result[0] = row_max[0]

    for j in range(1, m):
        if j == 1:
            result[j] = max(result[j - 1], row_max[j])
            continue
        result[j] = max(result[j - 1], result[j - 2] + row_max[j])

    print(result[-1])