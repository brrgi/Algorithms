import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

a = input()
b = input()
queue = deque()  # 앞에 꺼는 왼쪽 오른쪽 , 뒤에꺼는 n개의 칸 중 위치
queue.append([0, 0])
aVisit = [0 for _ in range(n)]
bVisit = [0 for _ in range(n)]
aVisit[0] = 1
now = -1

while queue:
    leng = len(queue)
    for i in range(leng):
        data = queue.popleft()
        # print(data)
        leftOrRight = data[0]
        jump = data[1]

        if (jump + 1) >= n or (jump + k) >= n:  # 성공 종료 조건
            # print(data, n, jump, k)
            print(1)
            exit()

        if leftOrRight == 0:  # left
            if a[jump + 1] == '1' and aVisit[jump + 1] == 0:  # 안전하고 방문 x
                queue.append([0, jump + 1])
                aVisit[jump + 1] = 1
            if jump>=1 and (jump - now) > 2 and a[jump - 1] == '1' and aVisit[jump - 1] == 0:
                # print(data, now)
                queue.append([0, jump - 1])
                aVisit[jump - 1] = 1
            if b[jump + k] == '1' and bVisit[jump + k] == 0:
                queue.append([1, jump + k])
                bVisit[jump + k] = 1
        else:
            if b[jump + 1] == '1' and bVisit[jump + 1] == 0:  # 안전하고 방문 x
                queue.append([1, jump + 1])
                bVisit[jump + 1] = 1
            if jump>=1 and (jump - now) > 2 and b[jump - 1] == '1' and bVisit[jump - 1] == 0:
                queue.append([1, jump - 1])
                # print("h2", data, now)
                bVisit[jump - 1] = 1
            if a[jump + k] == '1' and aVisit[jump + k] == 0:
                queue.append([0, jump + k])
                aVisit[jump + k] = 1

    now += 1

print(0)
