N = int(input())
fluids = sorted(list(map(int, input().split())))


ret = [0, 0, 0]
def search():
    start = 0
    end = N-1
    min_abs = float('inf')

    # left, right가 각각 N-1. N-2 인 상황까지 고려
    for pointer in range(N-2):
        start = pointer + 1
        end = N-1

        while start < end:

            cur_abs = fluids[start] + fluids[end] + fluids[pointer]

            if abs(min_abs) > abs(cur_abs):
                min_abs = cur_abs
                ret[0], ret[1], ret[2] = fluids[pointer], fluids[start], fluids[end]
            
            if cur_abs < 0: start += 1
            elif cur_abs > 0: end -= 1
            else: return

    return
search()
print(*ret)