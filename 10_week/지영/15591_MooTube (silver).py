from collections import deque


N, M = map(int, input().split())
tree = {}

for elm in range(N-1):
    v1, v2, cost = map(int, input().split())
    if v1 not in tree:
        tree[v1] = []
    if v2 not in tree:
        tree[v2] = []

    tree[v1].append([v2, cost])
    tree[v2].append([v1, cost])

def bfs(node: int):
    ret = 0

    queue = deque([node])
    visited = [False] * (N+1)
    visited[node] = True

    while queue:
        pop = queue.popleft()

        for col, cost in tree[pop]:

            if visited[col]: continue

            if cost < K: continue

            queue.append(col)
            visited[col] = True
            ret += 1
  
    return ret
    



for elm in range(M):
    """
        node와의 연결에서 그 cost가 K 이상인 노드

        반대로 이야기 하면, cost가 k 미만인 경우 해당 노드는 포함시킬 수 없다.
        이후에 나오는 값들 중, K 미만의 값이 있으면 포함 X
    """
    K, node = map(int, input().split())

    print(bfs(node))


