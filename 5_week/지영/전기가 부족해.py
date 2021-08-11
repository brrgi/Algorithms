node, edge, root = map(int, input().split());
roots = set(map(int, input().split()))
parents = [self for self in range(node+1)]
edges = sorted([list(map(int, input().split())) for _ in range(edge)], key=lambda edge: edge[2])
weight = 0

def getParent(node):
    if node == parents[node]: return node
    parents[node] = getParent(parents[node])
    return parents[node]

def isRoot(node):
    return node in roots

def isConnectable(s, e):
    # 부모가 갖거나, 각각의 부모가 서로 다른 발전소일 때, False
    start = getParent(s)
    end = getParent(e)
    if isRoot(start) and isRoot(end): return False
    if start == end: return False
    return True

def unionParent(s, e):
    """
        두 노드의 부모 노드가 전부 Root 노드가 아닌 다음의 경우를 보장합니다.
        - 한쪽만 Root 노드
        - 두 노드 모두 일반 노드
    """
    start = getParent(s)
    end = getParent(e)

    # 부모가 발전소인 노드의 경우, 우선순위가 더 높음
    isStartRoot = isRoot(start)
    isEndRoot = isRoot(end)

    if isStartRoot or not isEndRoot and start < end: parents[end] = start
    else: parents[start] = end


for elm in edges:
    if isConnectable(elm[0], elm[1]):
        unionParent(elm[0], elm[1])
        weight += elm[2]

print(weight)