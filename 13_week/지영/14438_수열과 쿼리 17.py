
class Node:
    def __init__(self, start, end, sum):
        # self.index = index
        self.start = start
        self.end = end
        self.min = sum


def insert(idx, start, end):
    if start == end:
        tree[idx] = Node(start, end, a_list[start])
        return
    
    tree[idx] = Node(start, end, min(a_list[start:end+1]))
    
    mid = (start + end) // 2
    insert(idx*2, start, mid)
    insert(idx*2+1, mid+1, end)

def update(idx, removed, updated, updated_idx):
    if len(tree)-1 < idx or not tree[idx]: 
        return
    
    if removed > tree[idx].min: tree[idx].min = min(tree[idx].min, updated)
    else: tree[idx].min = min(a_list[tree[idx].start: tree[idx].end+1])

    if (tree[idx].start + tree[idx].end) // 2 < updated_idx:
        update(idx*2+1, removed, updated, updated_idx)
    else:
        update(idx*2, removed, updated, updated_idx)

def prefix_min(idx, start, end):

    if tree[idx].start == start and tree[idx].end == end: return tree[idx].min
    # if tree[idx].start == start

    mid = (tree[idx].start + tree[idx].end) // 2

    # start - end 합이 좌측 노드에 포합되어 있는 경우
    if end <= mid:
        return prefix_min(idx*2, start, end)

    # start - end 합이 우측 노드에 포합되어 있는 경우
    elif mid < start:
        return prefix_min(idx*2+1, start, end)
    
    # start - mid - end의 순으로 되어 있는 경우
    else:
        return min(prefix_min(idx*2, start, mid), prefix_min(idx*2+1, mid+1, end))


N = int(input())
a_list = list(map(int, input().split()))
# N = random.randrange(1, 100001)
# a_list = [random.randrange(1, 10**9+1) for _ in range(N)] 



cnt = 0
while 2 ** cnt < len(a_list):
    cnt += 1

tree = [None] * (4*len(a_list))
insert(1, 0, len(a_list)-1)

answer = []
Q = int(input())
for _ in range(Q):
    op, i, j = map(int, input().split())

    if op == 1:
        past = a_list[i-1]
        a_list[i-1] = j

        update(1, past, j, i-1)
        continue
    
    if op == 2:
        print(prefix_min(1, i-1, j-1))
