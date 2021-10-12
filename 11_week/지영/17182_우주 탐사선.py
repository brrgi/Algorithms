
def backtrack(node, mask):
    ret = float('inf')
    for idx, elm in enumerate(graph[node]):
        if mask & 2**idx: continue

        if mask | 2**idx == breakpoint:
            return elm

        ret = min(ret, elm + backtrack(idx, mask | 2**idx))
    
    return ret



def get_small_idx(node: int, visited: list):
    min_val = float('inf')
    min_idx = 0
    for idx, elm in enumerate(graph[node]):
        if visited[idx]: continue
        if elm < min_val: 
            min_val = elm
            min_idx = idx
    
    return min_idx

def dijkstra(node: int):
    visited = [False] * N
    visited[node] = True

    for _ in range(N):
        idx = get_small_idx(node, visited)
        visited[idx] = True

        for idx1 in range(N):
            if idx1 == node or idx1 == idx: continue
            graph[node][idx1] = min(graph[node][idx1], graph[node][idx] + graph[idx][idx1])

"""
    다익스트라 + 비트마스킹
"""
def solution():
    global N
    N, M = map(int, input().split())

    global graph
    graph = [list(map(int, input().split())) for _ in range(N)]

    global breakpoint
    breakpoint = 0
    for idx in range(N):
        breakpoint += 2**idx

    for node in range(N):
        dijkstra(node)
    
    print(backtrack(M, 2**M))

solution()
