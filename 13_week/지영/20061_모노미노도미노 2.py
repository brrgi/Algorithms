import random
BLUE = 0
GREEN = 1
# GREEN = [[0] * 4 for _ in range(6)]
COL = 4
ROW = 6
FULL = 4

# BLUE, GREEN
BOARDS = [[[0] * COL for _ in range(ROW)], [[0] * COL for _ in range(ROW)]]


def check_special_place(type):
    """
        특별 공간의 블럭이 존재하는지 여부를 확인합니다.
        존재하는 수만큼의 개수를 반환합니다.
    """
    row_0 = 1 if sum(BOARDS[type][0]) else 0
    row_1 = 1 if sum(BOARDS[type][1]) else 0
    return row_0 + row_1

def remove_items(removed_row, cnt, type):
    """
        제거할 row를 기준으로 그 상위에 있는 모든 값을 아래로 복사합니다.
        자연스레 제거할 row 의 값은 그 상위의 row 값으로 대체됩니다.

        cnt: 상위 어떤 row의 값으로 대체하고자 할지 결정합니다.
    """

    for row in range(removed_row, -1, -1):
        if row - cnt < 0 :
            for col in range(COL):
                BOARDS[type][row][col] = 0
            continue
            
        for col in range(COL):
            BOARDS[type][row][col] = BOARDS[type][row-cnt][col]


def move_block_1_row_2_col(col_list, type):
    """
        초 - 1 * 2, 파 - 2 * 1
    """

    ret = 0
    row = 0
    for offset in range(ROW):
        NOT_EMPTY = 0
        for check in col_list:
            NOT_EMPTY |= BOARDS[type][offset][check]

        if NOT_EMPTY: break
        row = offset

    for col in col_list:
        BOARDS[type][row][col] = 1

    # check_full(type, col)
    # is full
    if sum(BOARDS[type][row]) == FULL:
        """
            하나의 row값의 합만 따져보면 됩니다.
        """
        # 점수 count
        ret += 1

        remove_items(row, 1, type)

    return ret


def move_block_1_col(col, op, type):
    """ 
        고정된 col의 값 [차지하는 row가 1개인지, 2인지는 모른다.]
        1 * 1, 초 - 2 * 1, 파 - 1 * 2

        op = -1 인 경우, 초 - 2 * 1, 파 - 1 * 2
        op = 0, 1 * 1
    """

    ret = 0
    # 블록이 차지하는 칸이 빨간색 칸의 경계를 넘어서는 경우는 주어지지 않는다.
    row = 0
    for offset in range(ROW):
        if BOARDS[type][offset][col]: break
        row = offset

    
    BOARDS[type][row][col] = 1
    if sum(BOARDS[type][row]) == FULL:
        ret += 1
        remove_items(row, 1, type)

    if op == 1: return ret

    if not ret:
        BOARDS[type][row-1][col] = 1
    else:
        BOARDS[type][row][col] = 1


    need_to_remove = []

    for i in range(0, -2, -1):
        # 반드시 더 아래에 있는 값부터 제거
        if sum(BOARDS[type][row+i]) == FULL:
            ret += 1
            need_to_remove.append(row+i)

    for _ in need_to_remove:
        remove_items(need_to_remove[0], 1, type)

    return ret
def solution():

    score = 0

    Q = int(input())
    for _ in range(Q):
        t, x, y = map(int, input().split())
        # 1 * 1 block
        if t == 1: 
            score += move_block_1_col(3-x, t, BLUE)
            score += move_block_1_col(y, t, GREEN)

        # 1 * 2 block
        elif t == 2:
            score += move_block_1_col(3-x, t, BLUE)
            score += move_block_1_row_2_col([y, y+1], GREEN)

        # 2 * 1 block
        else:
            score += move_block_1_row_2_col([3-x, 3-(x+1)], BLUE)
            score += move_block_1_col(y, t, GREEN)

        # special 위치에 있는지 검사
        b = check_special_place(BLUE) 
        g = check_special_place(GREEN)

        if b:
            remove_items(ROW-1, b, BLUE)
        if g:
            remove_items(ROW-1, g, GREEN)
        

    block = 0
    for board in (BOARDS):
        for b in board:
            block += sum(b)
    
    print(score)
    print(block)


solution()