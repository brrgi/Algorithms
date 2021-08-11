

def ret_row_max(row):
    memoization = [-1 for _ in range(len(row))]

    for idx, elm in enumerate(row):
        if idx == 0:
            memoization[idx] = elm
            continue
        if idx == 1:
            memoization[idx] = max(elm, memoization[idx-1])
            continue

        memoization[idx] = max(memoization[idx-2] + elm, memoization[idx-1])
    return memoization[len(row)-1]

def ret_candy_max(boxes):
    candy_set = []
    for row in boxes:
        candy_set.append(ret_row_max(row))
    return ret_row_max(candy_set)

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0: break

    boxes = [list(map(int, input().split())) for _ in range(N)]

    print(ret_candy_max(boxes))
