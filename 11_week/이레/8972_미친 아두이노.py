from collections import deque
from copy import deepcopy

dir = [(-2, -2), (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
r, c = map(int, input().split())
maps = [list(input()) for _ in range(r)]
numbers = input()

I = [0, 0]
R = deque()
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'I':
            I = [i, j]
        elif maps[i][j] == 'R':
            R.append([i, j])

start = 0
for number in numbers:
    start += 1
    # 1
    row, col = I[0], I[1]
    next_row, next_col = I[0] + dir[int(number)][0], I[1] + dir[int(number)][1]

    # 2
    if maps[next_row][next_col] == 'R':
        print('kraj', start)
        exit()
        break

    maps[row][col], maps[next_row][next_col] = maps[next_row][next_col],maps[row][col]
    I = [next_row, next_col]
    # 3
    new_R = deque()
    R_set = set()
    already_visit = []

    for i, j in R:
        if maps[i][j] != 'R':
            continue
        a, b = I[0] - i, I[1] - j
        if a < 0:
            a = -1
        elif a > 0:
            a = 1
        if b < 0:
            b = -1
        elif b > 0:
            b = 1

        next_row, next_col = i + a, j + b
        new_R.append([next_row, next_col])
        if maps[next_row][next_col] == 'I':
            print('kraj', start)
            exit()
            break

        if (next_row, next_col) not in R_set:
            R_set.add((next_row, next_col))
        else:
            already_visit.append([next_row, next_col])
        maps[i][j]='.'

    for i,j in new_R:
        maps[i][j]='R'

    for i in already_visit:  # 겹쳐있는 것들 다 터침
        maps[i[0]][i[1]] = '.'


    R = deepcopy(new_R)
for i in maps:
    for j in i:
        print(j, end='')
    print()
