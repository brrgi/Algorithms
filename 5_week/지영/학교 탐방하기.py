node, edge = map(int, input().split());
edges = sorted([list(map(int, input().split())) for _ in range(edge+1)], key=lambda edge: edge[2])

def getParent(node, parents):
    if node == parents[node]: return node
    parents[node] = getParent(parents[node], parents)
    return parents[node]

def retParentNodes(s, e, p):
    return getParent(s, p), getParent(e, p)

def isSameParent(s, e, parents):
    start, end = retParentNodes(s, e, parents)
    return start == end

def unionParent(s, e, parents):
    start, end = retParentNodes(s, e, parents)
    if start < end: parents[end] = start
    else: parents[start] = end

min_weight = 0
max_weight = 0

parents = [self for self in range(node+1)]
for elm in edges:
    if not isSameParent(elm[0], elm[1], parents):
        unionParent(elm[0], elm[1], parents)
        max_weight += 1 - elm[2]

parents = [self for self in range(node+1)]
for _ in range(len(edges)):
    elm = edges.pop()
    if not isSameParent(elm[0], elm[1], parents):
        unionParent(elm[0], elm[1], parents)
        min_weight += 1 - elm[2]


print(max_weight**2 - min_weight**2)