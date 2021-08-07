from itertools import combinations
from collections import deque
"""
    이 문제의 핵심: 
    1. 어떤 지점에 어떤 배양액을 놓을지 어떻게 선택할 것이냐 
    2. 모든 배양액들을 동시에 확장시키는 방법 -> 동시성 확보를 어떻게 할 것인가?
"""
N, M, G, R = map(int, input().split())
garden = []
available = []
for row in range(N):
    garden.append([])
    for col, val in enumerate(list(map(int, input().split()))):
        if val == 2:
            available.append([row, col])
        garden[row].append(val)
        


not_be_duplicated = [1, 0]
def count_flower(promising: deque, time: list, status: list) -> int:
    """
            [매개변수]
            - promising: 조합으로 선별된 시작 노드들이 담긴 deque 
            - time: 매 조합마다 초기화된 time list, 시작 시점들은 time = 0으로 초기화된 상태 
            - status: 현재 garden의 상태, [None -1, Green 0, Red 1, Flower 2]

            [가지치기]
            - 해당 노드가 접근할 수 없는 노드인 경우(한강인 경우, garden[row][col] == 0)
            - 이미 방문한 적 있는 경우
            - [동시성 확보]
            동일한 순서를 보장하기 위해 현재 몇번째 확산인지 마킹할 핑요가 있음. 이는 이전에 배양액을 뿌린 시점과 현 시점이 같은지 비교
            time[row][col] != nodes[3] + 1:
            time: 기존에 저장된 시점 정보
            nodes: 현 시점 정보
            - 이미 다른 색의 배양액이 해당 노드에 퍼져있는 경우 -> 꽃의 수를 count +1 해주고 pass
            
        """
    flower = 0
    while promising:
        nodes = promising.popleft()
        
        # 이 노드를 담기전 이전 노드들에서 이미 이곳에 접근해 꽃을 피운 경우가 있을 수 있으니 
        if status[nodes[0]][nodes[1]] == 2:
            continue

        
        for elm in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            row = nodes[0] + elm[0]
            col = nodes[1] + elm[1]

            if 0 > row or 0 > col or N-1 < row or M-1 < col: continue
            # 해당 노드가 한강인 경우,  접근할 수 없는 노드
            if garden[row][col] == 0: continue
            # 이미 해당 노드에 꽃을 피운 경우
            if status[row][col] == 2: continue

            if status[row][col] == 0 or status[row][col] == 1: #status -1인 상황을 배제하기 위함 
                # 현 노드가 Green이거나 Red이고, 같은 배양액이라면 continue
                if status[row][col] == nodes[2]: continue

                # 꽃을 만들기 이전에 서로 동시성이 보장되지 않은 경우. continue
                if time[row][col] != nodes[3] + 1 : continue

                # 이미 해당 노드에 다른 배양액에 접근한 상태라면, count +1해주고 따로 담지않고 continue
                if status[row][col] == not_be_duplicated[nodes[2]]:
                    flower += 1
                    status[row][col] = 2
                    continue

            promising.append([row, col, nodes[2], nodes[3] + 1])
            # 현 시점의 타임 정보를 업데이트
            time[row][col] = nodes[3] + 1
            status[row][col] = nodes[2]

    return flower

ret = 0
for selected in list(combinations(available, G + R)):
    for green in list(combinations(selected, G)):
        queue = deque()
        # None -1 Green 0 Red 1 Flower 2
        status = [[-1]*M for _ in range(N)]
        # 동시성 보장을 위한 time count
        time = [[-1]*M for _ in range(N)]
        for elm in selected:
            if elm in green: 
                queue.append([elm[0], elm[1], 0, 0])
                status[elm[0]][elm[1]] = 0
            else: 
                queue.append([elm[0], elm[1], 1, 0])
                status[elm[0]][elm[1]] = 1
            time[elm[0]][elm[1]] = 0
        ret = max(ret, count_flower(queue, time, status))

print(ret)