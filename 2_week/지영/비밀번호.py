n, m = map(int, input().split())
needed = list(map(int, input().split()))
counts = [0,0,0,0,0,0,0,0,0,0,0]
def back_track(located):
    count = 0
    if located == n:
        for elm in needed:
            if counts[elm] == 0:
                return 0
        return 1

    for elm in range(10):
        counts[elm] += 1
        count += back_track(located +1)
        counts[elm] -= 1
    return count

print(back_track(0))
