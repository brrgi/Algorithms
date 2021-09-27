from copy import deepcopy
import heapq
import sys
from collections import defaultdict
INF = sys.maxsize


def solution(n, start, end, roads, traps):
    set_traps = set(traps)
    distance = [[] for _ in range(n + 1)]
    come=[[] for i in range(n+1)]
    go=[[] for i in range(n+1)]
    for road in roads:
        s, e, dist = road
        go[s].append(e)
        come[e].append(s)
        distance[s].append([e, dist])
    print(go)
    print(come)
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


n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2]
print(solution(n, start, end, roads, traps))
