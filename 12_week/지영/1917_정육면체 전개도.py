from collections import deque
import copy

RIGHT = 0
TOP = 1
LEFT = 2
BOTTOM = 3

exchange = [LEFT, BOTTOM, RIGHT, TOP]

position = {
    # order: 오, 위, 왼, 아래
    1: deque([3, 5, 2, 4]),
    2: deque([5, 6, 4, 1]),
    3: deque([4, 6, 5, 1]),
    4: deque([2, 6, 3, 1]),
    5: deque([3, 6, 2, 1]),
    6: deque([2, 5, 3, 4])

}

# order: 오, 위, 왼, 아래
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def get_order(elm: int, dir: int, n: int):
    """
        특정 위치에 원하는 값이 놓일때까지 쉬프트해 명확한 값을 기준으로 방향을 재정의합니다.
    """
    pos = copy.deepcopy(position[elm])

    # dir 위치에 n 값이 놓일때까지 shift
    while pos[exchange[dir]] != n:
        pos.rotate(-1)
    
    return pos


def is_cube(row, col) -> bool:
    check = set()

    queue = deque()
    queue.append([row, col, 1, position[1]])
    check.add(1)
    visited[row][col] = True

    while queue:
        c_r, c_c, n, order = queue.popleft()
        
        for elm in range(4):
            n_r = c_r + dr[elm]
            n_c = c_c + dc[elm]

            if n_r < row or n_r > 6 * (row // 6) + 5 or n_c < 0 or n_c > 5: continue
            if visited[n_r][n_c]: continue

            if maps[n_r][n_c]:
                if order[elm] in check: return 'no'
                check.add(order[elm])

                shift = get_order(order[elm], elm, n)
                queue.append([n_r, n_c, order[elm], shift])
                visited[n_r][n_c] = True
    
    return 'yes' if len(check) == 6 else 'no'


# maps = [list(map(int, input().split())) for _ in range(6)]
maps = [list(map(int, input().split())) for _ in range(18)]
visited = [[False] * 6 for _ in range(18)]

for s in range(0, 18, 6):
    flag = True
    
    for row in range(s, s+6):
        if not flag: 
            break
        for col in range(6):
            if maps[row][col] and not visited[row][col]: 
                print(is_cube(row, col))
                flag = False
                break
