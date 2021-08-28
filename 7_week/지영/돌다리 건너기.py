from collections import deque

PATH = input()

indexing = {
    'R':[deque(), deque()], 
    'I':[deque(), deque()], 
    'N':[deque(), deque()], 
    'G':[deque(), deque()], 
    'S':[deque(), deque()]
    }

bridge_len = 0
for idx in range(2):
    bridge = input()
    bridge_len = len(bridge)
    for b_idx, elm in enumerate(bridge):
        indexing[elm][idx].appendleft(b_idx)

# 시점을 같이 저장, cache 시간 초과의 원인
cache = [[[-1]* bridge_len for _ in range(2)]for _ in range(len(PATH)+1)]
def check_reachable(node_idx: int, which: int, cnt: int):
    """
        node는 결로에 있는 값만 전달됨을 보장합니다.

        [arguments]
            node: 현재 돌다리 위치(string)
            node_idx: 현재 돌다리 위치(idx: int)
            which: 다리 종류 
    """

    if cache[cnt][which][node_idx] != -1: return cache[cnt][which][node_idx]

    #  남은 문자열의 개수 , 현재의 노드 인덱스
    if len(PATH) - cnt > node_idx: 
        cache[cnt][which][node_idx] = 0
        return cache[cnt][which][node_idx]

    if cnt == len(PATH):
        cache[cnt][which][node_idx] = 1
        return cache[cnt][which][node_idx]
    
    ret = 0

    # 현재 위치에서 갈 수 있는 모든 노드들을 파악한 뒤, 이 노드들을 대상으로 DFS를 한다.
    for elm in indexing[PATH[len(PATH) - (cnt+1)]][which^1]:
        if elm >= node_idx: continue
        ret += check_reachable(elm, which^1, cnt+1)

    cache[cnt][which][node_idx] = ret
    return cache[cnt][which][node_idx]

cnt = 1
case = 0
# start
for idx in range(2):
    for elm in indexing[PATH[len(PATH)-cnt]][idx]:  
        case += check_reachable(elm, idx, cnt)
print(case)
