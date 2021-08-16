import sys
from collections import defaultdict
from heapq import *
input = sys.stdin.readline


def prim(edges, start_node):
    value = 0
    visit = [False for _ in range(n + 1)]
    visit[start_node] = True
    candidate_edge_list = edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n2 = heappop(candidate_edge_list)

        if visit[n2]:       #둘다 이미 방문했기에
            continue

        visit[n2] = True
        value += weight

        for edge in edges[n2]:
            if visit[edge[1]]:
                continue
            heappush(candidate_edge_list, edge)
    return value


n, m = map(int, input().split())
min_edges = defaultdict(list)
max_edges = defaultdict(list)

for i in range(m + 1):
    u, v, weight = map(int, input().split())

    min_edges[u].append((weight ^ 1, v))
    min_edges[v].append((weight ^ 1, u))

    max_edges[u].append((weight, v))
    max_edges[v].append((weight, u))

min_val = prim(min_edges, 0)
# print(min_val)
# print("------------------------")
max_val = prim(max_edges, 0)
# print(max_val)
# print(n-min_val, max_val)
print(((n - max_val) ** 2) - min_val ** 2)
