import heapq
import sys
n,p,k=map(int,input().split())
INF=sys.maxsize
distance=[[] for _ in range(n+1)]
for i in range(p):
    start,end,dist=map(int,input().split())
    distance[start].append([end, dist])


def dijkstra():
    global K_distance, end
    queue = []
    # K_distance = [INF for _ in range(V + 1)]
    # K_distance[K] = 0  # 자기자신
    # heapq.heappush(queue, [0, K])  # 자기 자신이 우선순위 큐      [거리, 정점]
    while queue:
        mid = heapq.heappop(queue)
        for end in distance[mid[1]]:
            if K_distance[end[0]] > mid[0] + end[1]:
                K_distance[end[0]] = mid[0] + end[1]
                heapq.heappush(queue, [K_distance[end[0]], end[0]])
