n = int(input())
red = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
red_90 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
green = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
blue = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
now = []
number = 0


def init(number, row, col):
    if number == 1:
        red[row][col] = 1
    if number == 2:
        red[row][col] = 1
        red[row][col + 1] = 1
    if number == 3:
        red[row][col] = 1
        red[row + 1][col] = 1


def zero():
    global red
    global red_90
    red = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    red_90 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = m[r][c]
    return ret


for i in range(n):
    t, x, y = map(int, input().split())
    init(t, x, y)
    red_90 = rotate_90(red)

    red_row = 0
    red_90_row = 0
    green_row = 5
    blue_row = 5

    now1 = []
    now2 = []
    for i in range(4):
        for j in range(4):
            if red[i][j] == 1:
                now1.append([i, j])
            if red_90[i][j] == 1:
                now2.append([i, j])
    if len(now1) == 2:
        if now1[0][0] > now1[1][0]:
            now1.reverse()
    if len(now2) == 2:
        if now2[0][0] > now2[1][0]:
            now2.reverse()
    zero()
    temp1 = red + green
    temp2 = red_90 + blue

    while 1:
        check = 0
        next = []
        for row, col in now1:
            if row == 9:  # 마지막 줄 도달
                check = 1
                break
            if temp1[row + 1][col] == 1:  # 다음 줄 못감
                check = 1
                break
            else:
                next.append([row + 1, col])
        if check == 0:
            now1 = next[:]
        else:
            break
    for row, col in now1:
        temp1[row][col] = 1
    g = []
    for i in range(4, 10):
        if temp1[i].count(1) == 0:
            continue
        if temp1[i].count(1) == 4:
            number += 1
            continue
        g.append(temp1[i])

    if len(g) == 6 or len(g) == 5:
        green = [[0, 0, 0, 0], [0, 0, 0, 0]] + g[:4]
    else:
        green = [[0, 0, 0, 0] for _ in range(6 - len(g))] + g

    while 1:
        check = 0
        next = []
        for row, col in now2:
            if row == 9:  # 마지막 줄 도달
                check = 1
                break
            if temp2[row + 1][col] == 1:  # 다음 줄 못감
                check = 1
                break
            else:
                next.append([row + 1, col])
        if check == 0:
            now2 = next[:]
        else:
            break

    for row, col in now2:
        temp2[row][col] = 1
    g = []
    for i in range(4, 10):
        if temp2[i].count(1) == 0:
            continue
        if temp2[i].count(1) == 4:
            number += 1
            continue
        g.append(temp2[i])
    if len(g) == 6 or len(g) == 5:
        blue = [[0, 0, 0, 0], [0, 0, 0, 0]] + g[:4]
    else:
        blue = [[0, 0, 0, 0] for _ in range(6 - len(g))] + g


    # print("시작")
    # for i in green:
    #     print(i)
    # print("중간")
    # for i in blue:
    #     print(i)
    # print("------------")
result = 0
for i in range(6):
    for j in range(4):
        result += blue[i][j] + green[i][j]
print(number)
print(result)
