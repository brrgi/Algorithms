from collections import deque
N, A, B = map(int, input().split())


# [0] = 현 위치, [1] = timeline, [2] = 어떤 동물의 접근이지 파악 목적 0 오리, 1 육리
queue = deque()
queue.append([A, 1, 0])
queue.append([B, 1, 1])

# 이동 와중에 동시성만 챙기면 되니, timeline만 확인 어차피 한번 지나간 시간은 중복되지 않으니 중복될 걱정 X
time = [[1] * (N+1) for _ in range(2)]
flag = False
while queue and not flag:

    cur_pos, timeline, kind= queue.popleft()

    for elm in [-2**(timeline-1), 2**(timeline-1)]:
        if cur_pos + elm < 1 or cur_pos + elm > N: continue

        if time[kind^1][cur_pos + elm] == timeline + 1:
            print(timeline)
            flag = True
            break

        queue.append([cur_pos + elm, timeline + 1, kind])
        time[kind][cur_pos + elm] = timeline + 1
    
if not flag: print(-1)