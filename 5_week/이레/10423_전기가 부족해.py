n, m, k = map(int, input().split())
number = set(map(int, input().split()))
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

def find(node):
    if parent[node] != node:
        return find(parent[node])
    return parent[node]

def union(node_a, node_b):
    root_a = find(node_a)
    root_b = find(node_b)

    if root_a in number:            #1. a의 root가 발전소일 때
        parent[root_b]=root_a
    else:
        parent[root_a]=root_b       #2. b의 root가 발전소일 때


def kruskal(graph):
    mst = []

    for node in graph['vertices']:
        parent[node] = node
    edges = graph['edges']
    edges.sort(key=lambda x:x[0])        #weight 기준으로 정렬


    for edge in edges:
        weight, node_a, node_b = edge
        if find(node_a) in number and find(node_b) in number:       #root가 둘 다 발전소일 때
            continue
        if find(node_a) != find(node_b):        #부모가 서로 다를 때
            union(node_a, node_b)               #합치기
            mst.append(edge)

    return mst

result=0
for i in kruskal(graph):
    result+=i[0]
print(result)