n, m, k = map(int, input().split())
number = list(map(int, input().split()))
graph={
    'vertices':[
        i+1 for i in range(n)
    ],
    'edges':[

    ]
}
for i in range(m):
    u, v, w = map(int, input().split())
    graph['edges'].append((w,u,v))

# 부모 노드 값 저장
parent = dict()
# 각각의 노드의 높이 번호
rank = dict()

def initialization(node):
    parent[node] = node
    rank[node] = 0

def find(node):
    # path compression
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_a, node_b):
    # union-by-rank
    root_a = find(node_a)
    root_b = find(node_b)

    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1

def kruskal(graph):
    mst = []

    # 초기화
    for node in graph['vertices']:
        initialization(node)
    # 간선을 오름차순으로 정렬
    edges = graph['edges']
    edges.sort()        #weight 기준으로 정렬

    # 사이클 확인 후 연결
    for edge in edges:
        weight, node_a, node_b = edge
        if find(node_a) != find(node_b):
            union(node_a, node_b)
            mst.append(edge)

    return mst

print(kruskal(graph))