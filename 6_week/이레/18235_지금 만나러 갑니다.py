from collections import deque

n, a, b = map(int, input().split())

five_queue = deque()
five_queue.append(a)
six_queue = deque()
six_queue.append(b)

visit = [[-1 for _ in range(500001)] for _ in range(2)]  # a,b visit 2개
result=-1

def bfs(start):
    # print("------------------")
    if len(five_queue)==0 or len(six_queue)==0:
        return -1
    leng1=len(five_queue)
    for i in range(leng1):
        data = five_queue.popleft()

        if data - (2 ** start) >= 1:
            visit[0][data - (2 ** start)] = start
            five_queue.append(data - (2 ** start))
        if data + (2 ** start) < 500001:
            visit[0][data + (2 ** start)] = start
            five_queue.append(data + (2 ** start))

    leng2=len(six_queue)
    for i in range(leng2):
        data = six_queue.popleft()

        if data - (2 ** start) >= 1:
            visit[1][data - (2 ** start)] = start
            six_queue.append(data - (2 ** start))
        if data + (2 ** start) < 500001:
            visit[1][data + (2 ** start)] = start
            six_queue.append(data + (2 ** start))

    # print(2**start, five_queue, six_queue)
    for i in range(1, 500001):
        if visit[0][i]!=-1:
            if visit[0][i]==visit[1][i]:
                return visit[0][i]
    return 0
for i in range(30):
    t=bfs(i)

    if t==-1:
        result=-1
        break
    elif t!=0:
        result=t+1
        break
print(result)
