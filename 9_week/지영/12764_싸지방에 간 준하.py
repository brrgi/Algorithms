import heapq
from collections import deque

N = int(input())
prev = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda elm: elm[0])
period = deque(prev)
last_time = prev[-1][0]

answer = [0] * N
end_priority = []
chair_priority = []
# heapq.heappush(end_priority, (0, 0))

for chair in range(N):
    heapq.heappush(chair_priority, chair)

# end time, which chair
for start, end in period:

    while end_priority:
        e, c = heapq.heappop(end_priority)
        if e > start:
            heapq.heappush(end_priority, (e, c))
            break
        heapq.heappush(chair_priority, c)

    # 현재 가능한 의자 숫자가 작은 것부터 뽑기
    # [아무도 사용하지 않은 의자, 이미 사용이 끝난 의자]
    available = heapq.heappop(chair_priority)

    # 해당 의자를 끝나는 시간이 e인 사람이 이용하기
    heapq.heappush(end_priority, (end, available))

    # 사용한 의자 카운트
    answer[available] += 1

res = list(filter(lambda x: x > 0, answer))
print(len(res))
print(' '.join(map(str, res)))