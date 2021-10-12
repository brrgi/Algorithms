"""
4 5
I....
.....
.R.R.
.....
6
"""

JONGSU = 'I'
MAD = 'R'

R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]

adi = set()

for row in range(R):
    for col in range(C):
        if maps[row][col] == JONGSU:
            j = (row, col)
        if maps[row][col] == MAD:
            adi.add((row, col))


directions = list(map(int, input()))

dr = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

def moved_adi(r, c):
    min = 200
    ret = [0, 0]

    for dir in range(9):
        n_r = r + dr[dir]
        n_c = c + dc[dir]

        if n_r < 0 or n_r > R-1 or n_c < 0 or n_c > C-1: continue

        val  = abs(n_r - j[0]) + abs(n_c - j[1])

        if val < min:
            # 절대값이 같은 경우는?
            min = val
            ret = (n_r, n_c)

    return ret

flag = True
for idx, direction in enumerate(directions):
    if not flag: break

    j = (j[0]+ dr[direction-1], j[1] + dc[direction-1])

    # 종수의 이동이 아두이노의 위치와 일치 여부
    if j in adi: 
        print(f"kraj {idx+1}")
        flag = False
        break

    new_adi = set()
    removed = set()
    for r, c in adi:
        moved = moved_adi(r, c)

        # 종수 위치와 일치 여부
        if moved == j:
            print(f"kraj {idx+1}")
            flag = False
            break
        
        # 아두이노 파괴
        if moved in new_adi:
            new_adi.remove(moved)
            removed.add(moved)
            continue
        
        if moved not in removed:
            new_adi.add(moved)

    adi = new_adi

if flag:
    ret = [['.'] * C for _ in range(R)]
    ret[j[0]][j[1]] = JONGSU

    for row, col in adi:
        ret[row][col] = MAD

    for row in ret:
        print(''.join(row))


