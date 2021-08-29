import heapq
import sys
from collections import defaultdict
INF = sys.maxsize


def solution(n, start, end, roads, traps):
    set_traps = set(traps)
    distance = [[] for _ in range(n + 1)]
    list_dict=defaultdict(list)
    for i in set_traps:
        list_dict[i]        #값을 지정하지 않으면 빈 리스트 생성
    for road in roads:
        s, e, dist = road
        if e in set_traps:
            list_dict[e].append(s)
        distance[s].append([e, dist])

    queue = []
    k_distance = [INF for _ in range(n + 1)]
    k_distance[start] = 0
    heapq.heappush(queue, [0, start])   #거리, 시작 위치
    while queue:
        mid=heapq.heappop(queue)    #거리 시작위치
        trap_list=[]
        if mid[1] in set_traps:     #mid[1]은 현재 trap 위치
            for i in range(n+1):
                if i==mid[1]:
                    for j in distance[i]:
                        trap_list.append([,i,])    #start, end , 거리
                    continue
                else:
                    for j in distance[i]:
                        if j[0]=


        for end in distance[mid[1]]:
            if k_distance[end[0]]>mid[0]+end[1]:
                k_distance[end[0]]=mid[0]+end[1]
                heapq.heappush(queue, [k_distance[end[0]], end[0]])

    answer = 0
    return answer


n = 3
start = 1
end = 3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]
print(solution(n, start, end, roads, traps))
