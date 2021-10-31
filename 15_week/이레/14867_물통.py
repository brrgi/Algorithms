from collections import deque


def bfs():
    if c + d == 0:
        return 0

    while queue:
        q, w = queue.popleft()

        # a 채움, 비움
        if (a, w) not in visit.keys():
            queue.append((a, w))
            visit[(a, w)] = visit[(q, w)] + 1

        if (0, w) not in visit.keys():
            queue.append((0, w))
            visit[(0, w)] = visit[(q, w)] + 1

        # b 채움, 비움
        if (q, b) not in visit.keys():
            queue.append((q, b))
            visit[(q, b)] = visit[(q, w)] + 1

        if (q, 0) not in visit.keys():
            queue.append((q, 0))
            visit[(q, 0)] = visit[(q, w)] + 1

        # 이동
        if q <= b - w:
            if (0, q + w) not in visit.keys():
                queue.append((0, q + w))
                visit[(0, q + w)] = visit[(q, w)] + 1
        else:
            if (q + w - b, b) not in visit.keys():
                queue.append((q + w - b, b))
                visit[(q + w - b, b)] = visit[(q, w)] + 1

        if w <= a - q:
            if (q + w, 0) not in visit.keys():
                queue.append((q + w, 0))
                visit[(q + w, 0)] = visit[(q, w)] + 1
        else:
            if (a, q + w - a) not in visit.keys():
                queue.append((a, q + w - a))
                visit[(a, q + w - a)] = visit[(q, w)] + 1

        if (c, d) in visit.keys():
            if visit[(q, w)] > 0:
                return visit[(q, w)]

    return -1


a, b, c, d = map(int, input().split())
visit = dict()
queue = deque()
queue.append((0, 0))
visit[(0, 0)] = 1

print(bfs())
