#3시 50분 -> 4시 5분
import heapq
import sys
INF=sys.maxsize

#n은 V, s 시작, a집, b집 ,fares(간선)
def solution(n, s, a, b, fares):
    INF = sys.maxsize
    distance = [[] for _ in range(n + 1)]

    for start, end, dist in fares:
        distance[start].append([end, dist])
        distance[end].append([start, dist])

    all=[]
    for i in range(1, n+1):
        queue = []
        K_distance = [INF for _ in range(n + 1)]
        K_distance[i] = 0  # 자기자신
        heapq.heappush(queue, [0, i])  # 자기 자신이 우선순위 큐      [거리, 정점]
        while queue:
            mid = heapq.heappop(queue)
            for end in distance[mid[1]]:
                if K_distance[end[0]] > mid[0] + end[1]:
                    K_distance[end[0]] = mid[0] + end[1]
                    heapq.heappush(queue, [K_distance[end[0]], end[0]])
        K_distance.pop(0)
        all.append(K_distance)
    for i in all:
        print(i)
    min_value=all[s-1][a-1]+all[s-1][b-1]


    for i in range(n):
        val=all[s-1][i]
        val+=all[i][a-1]+all[i][b-1]
        min_value=min(min_value, val)

    answer = min_value
    return answer



n=6
s=4
a=6
b=2
fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))