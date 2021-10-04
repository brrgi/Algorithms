from itertools import combinations
from collections import deque

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
maps = [list(input()) for _ in range(5)]
numbers = [i for i in range(25)]
result = 0

comb = combinations(numbers, 7)  # 25C7 = 480700(사십팔만)


def numToLoc(number):
    return [number // 5, number % 5]


def locToNum(r, c):
    return (r * 5) + c


for nums in comb:
    temp = []
    visit = [0 for _ in range(7)]
    for num in nums:
        temp.append(numToLoc(num))

    # rule 1 -> S가 4이상인지
    s = 0
    for t in temp:
        if maps[t[0]][t[1]] == 'S':
            s += 1
    if s < 4: continue

    # rule 2 -> 다 이어져있는지
    queue = deque()
    queue.append(temp[0])
    visit[0] = 1
    cnt = 1
    while queue:
        data = queue.popleft()
        for r, c, in dir:
            next_r = data[0] + r
            next_c = data[1] + c

            if 0 <= next_r < 5 and 0 <= next_c < 5:
                # print(nums, locToNum(next_r, next_c), next_r, next_c)
                if locToNum(next_r, next_c) not in nums:
                    continue
                if visit[nums.index(locToNum(next_r, next_c))] == 0:
                    visit[nums.index(locToNum(next_r, next_c))] = 1
                    cnt+=1
                    queue.append([next_r, next_c])

    if cnt==7:
        result+=1

print(result)

