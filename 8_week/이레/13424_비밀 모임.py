import heapq
import sys
t = int(input())
INF=sys.maxsize
for i in range(t):
    n, m = map(int, input().split())
    result=[0 for _ in range(n)]
    distance = [[] for _ in range(n + 1)]  # 정점갯수 + 1
    secrets = []
    for i in range(m):
        start, end, dist=map(int, input().split())
        distance[start].append([end, dist])
        distance[end].append([start, dist])
    input()
    friends = list(map(int, input().split()))


    for k in friends:
        queue=[]
        k_distance=[INF for _ in range(n+1)]
        k_distance[k]=0
        heapq.heappush(queue, [0,k])
        while queue:
            mid=heapq.heappop(queue)
            for end in distance[mid[1]]:    #mid[1]은 현재 위치
                if k_distance[end[0]]>mid[0]+end[1]:
                    k_distance[end[0]]=mid[0]+end[1]
                    heapq.heappush(queue, [k_distance[end[0]], end[0]])

        for i in range(n):
            result[i]+=k_distance[i+1]
    print(result.index(min(result))+1)